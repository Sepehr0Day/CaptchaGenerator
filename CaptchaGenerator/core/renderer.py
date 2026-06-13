from __future__ import annotations

import math
import random
from collections.abc import Sequence
from dataclasses import dataclass
from typing import Callable

from PIL import Image, ImageDraw, ImageFilter, ImageFont

from CaptchaGenerator.core.constants import DIFFICULTIES, STYLES
from CaptchaGenerator.exceptions import InvalidArgumentError

DEFAULT_SIZE = (720, 240)


@dataclass(frozen=True)
class RenderSettings:
    rotation: float
    vertical_jitter: int
    wave_amplitude: tuple[float, float]
    curve_count: tuple[int, int]
    speckle_density: float
    stroke_divisor: int
    spacing: tuple[int, int]


DIFFICULTY_SETTINGS = {
    "easy": RenderSettings(5, 5, (0.0, 2.0), (1, 1), 0.0005, 65, (8, 13)),
    "medium": RenderSettings(13, 13, (3.0, 7.0), (2, 3), 0.0015, 45, (3, 11)),
    "hard": RenderSettings(19, 18, (6.0, 11.0), (3, 5), 0.0024, 37, (-1, 8)),
    "extreme": RenderSettings(27, 24, (9.0, 16.0), (5, 7), 0.0035, 31, (-5, 6)),
}


def validate_text_request(
    *,
    length: int,
    values: str,
    fonts: Sequence[str],
) -> None:
    if length <= 0:
        raise InvalidArgumentError("number_gen must be greater than zero.")
    if not values:
        raise InvalidArgumentError("values_captcha must not be empty.")
    if not fonts:
        # An empty list is supported through the system-font fallback.
        return


def create_background(source: Image.Image | None = None) -> Image.Image:
    width, height = DEFAULT_SIZE
    if source is not None:
        return source.convert("RGB").resize(DEFAULT_SIZE, Image.Resampling.LANCZOS)

    hue = random.randint(205, 245)
    base = _hsv_to_rgb(hue / 360, random.uniform(0.08, 0.18), random.uniform(0.90, 0.98))
    accent = _hsv_to_rgb(
        ((hue + random.randint(-25, 25)) % 360) / 360,
        random.uniform(0.08, 0.20),
        random.uniform(0.82, 0.94),
    )
    image = Image.new("RGB", DEFAULT_SIZE)
    pixels = image.load()
    if pixels is None:
        raise RuntimeError("Unable to access background pixels.")
    for y in range(height):
        ratio = y / max(height - 1, 1)
        for x in range(width):
            wave = math.sin((x / width) * math.pi * 2) * 0.025
            mix = min(1.0, max(0.0, ratio + wave))
            pixels[x, y] = tuple(
                int(base[channel] * (1 - mix) + accent[channel] * mix)
                for channel in range(3)
            )
    return image.filter(ImageFilter.GaussianBlur(0.8))


def render_captcha(
    text: str,
    *,
    font_loader: Callable[[list[str], int], ImageFont.FreeTypeFont],
    fonts: list[str],
    background: Image.Image | None = None,
    preferred_colors: Sequence[str] | None = None,
    difficulty: str = "medium",
    style: str = "modern",
) -> Image.Image:
    if not text:
        raise InvalidArgumentError("Captcha text must not be empty.")

    settings = get_render_settings(difficulty, style)
    image = create_background(background)
    width, height = image.size
    draw = ImageDraw.Draw(image, "RGBA")
    palette = _text_palette(preferred_colors)

    _draw_style_background(draw, width, height, palette, style, settings)
    text_layer = Image.new("RGBA", image.size, (0, 0, 0, 0))
    font_size = _fit_font_size(text, font_loader, fonts, width, height)
    cursor = _text_start(text, font_loader, fonts, font_size, width)

    for index, char in enumerate(text):
        font = font_loader(fonts, random.randint(max(34, font_size - 5), font_size + 5))
        bbox = font.getbbox(char)
        char_width = max(1, int(bbox[2] - bbox[0]))
        char_height = max(1, int(bbox[3] - bbox[1]))
        tile = Image.new("RGBA", (char_width + 36, char_height + 42), (0, 0, 0, 0))
        tile_draw = ImageDraw.Draw(tile)
        color = random.choice(palette)
        tile_draw.text(
            (18 - bbox[0], 16 - bbox[1]),
            char,
            font=font,
            fill=color,
            stroke_width=max(1, font_size // settings.stroke_divisor),
            stroke_fill=(20, 25, 35, 185),
        )
        tile = tile.rotate(
            random.uniform(-settings.rotation, settings.rotation),
            resample=Image.Resampling.BICUBIC,
            expand=True,
        )
        y = (height - tile.height) // 2 + random.randint(
            -settings.vertical_jitter, settings.vertical_jitter
        )
        text_layer.alpha_composite(tile, (int(cursor), y))
        cursor += char_width + random.randint(*settings.spacing)

    text_layer = _wave_distort(text_layer, settings)
    image = Image.alpha_composite(image.convert("RGBA"), text_layer)
    draw = ImageDraw.Draw(image, "RGBA")
    _draw_style_foreground(draw, width, height, palette, style, settings)
    _draw_speckles(draw, width, height, settings.speckle_density)
    return image.convert("RGB").filter(ImageFilter.UnsharpMask(radius=1.1, percent=120))


def get_render_settings(difficulty: str, style: str) -> RenderSettings:
    normalized_difficulty = difficulty.lower()
    normalized_style = style.lower()
    if normalized_difficulty not in DIFFICULTY_SETTINGS:
        choices = ", ".join(DIFFICULTIES)
        raise InvalidArgumentError(f"difficulty must be one of: {choices}.")
    if normalized_style not in STYLES:
        choices = ", ".join(STYLES)
        raise InvalidArgumentError(f"style must be one of: {choices}.")
    return DIFFICULTY_SETTINGS[normalized_difficulty]


def _fit_font_size(
    text: str,
    font_loader: Callable[[list[str], int], ImageFont.FreeTypeFont],
    fonts: list[str],
    width: int,
    height: int,
) -> int:
    for size in range(int(height * 0.62), 31, -2):
        font = font_loader(fonts, size)
        total = sum(max(1, font.getbbox(char)[2] - font.getbbox(char)[0]) + 9 for char in text)
        if total <= width * 0.82:
            return size
    return 32


def _text_start(
    text: str,
    font_loader: Callable[[list[str], int], ImageFont.FreeTypeFont],
    fonts: list[str],
    size: int,
    width: int,
) -> float:
    font = font_loader(fonts, size)
    total = sum(max(1, font.getbbox(char)[2] - font.getbbox(char)[0]) + 7 for char in text)
    return max(22.0, (width - total) / 2)


def _wave_distort(layer: Image.Image, settings: RenderSettings) -> Image.Image:
    width, height = layer.size
    amplitude = random.uniform(*settings.wave_amplitude)
    if amplitude == 0:
        return layer
    period = random.uniform(90.0, 150.0)
    phase = random.uniform(0, math.pi * 2)
    output = Image.new("RGBA", layer.size, (0, 0, 0, 0))
    for x in range(width):
        offset = int(amplitude * math.sin((x / period) * math.pi * 2 + phase))
        strip = layer.crop((x, 0, x + 1, height))
        output.paste(strip, (x, offset))
    return output


def _draw_texture(draw: ImageDraw.ImageDraw, width: int, height: int) -> None:
    for _ in range(18):
        x = random.randint(0, width)
        y = random.randint(0, height)
        radius = random.randint(18, 75)
        draw.ellipse(
            (x - radius, y - radius, x + radius, y + radius),
            fill=(255, 255, 255, random.randint(3, 11)),
        )


def _draw_style_background(
    draw: ImageDraw.ImageDraw,
    width: int,
    height: int,
    palette: Sequence[tuple[int, int, int, int]],
    style: str,
    settings: RenderSettings,
) -> None:
    if style != "minimal":
        _draw_texture(draw, width, height)
    if style == "mesh":
        gap = 28 if settings.speckle_density < 0.002 else 20
        color = (*random.choice(palette)[:3], 35)
        for x in range(0, width, gap):
            draw.line((x, 0, x, height), fill=color, width=1)
        for y in range(0, height, gap):
            draw.line((0, y, width, y), fill=color, width=1)


def _draw_style_foreground(
    draw: ImageDraw.ImageDraw,
    width: int,
    height: int,
    palette: Sequence[tuple[int, int, int, int]],
    style: str,
    settings: RenderSettings,
) -> None:
    if style == "minimal":
        _draw_curves(draw, width, height, palette, (0, 1))
    elif style == "arc":
        _draw_arcs(draw, width, height, palette, settings.curve_count)
    elif style == "mesh":
        _draw_curves(draw, width, height, palette, (1, 2))
        _draw_cross_lines(draw, width, height, palette, settings.curve_count)
    elif style == "wave":
        low, high = settings.curve_count
        _draw_curves(draw, width, height, palette, (low + 1, high + 2))
    else:
        _draw_curves(draw, width, height, palette, settings.curve_count)


def _draw_curves(
    draw: ImageDraw.ImageDraw,
    width: int,
    height: int,
    palette: Sequence[tuple[int, int, int, int]],
    count: tuple[int, int],
) -> None:
    for _ in range(random.randint(*count)):
        points = []
        center = random.randint(height // 3, height * 2 // 3)
        amplitude = random.randint(14, 34)
        phase = random.uniform(0, math.pi * 2)
        period = random.uniform(65, 105)
        for x in range(-20, width + 21, 8):
            y = center + int(amplitude * math.sin(x / period + phase))
            points.append((x, y))
        color = random.choice(palette)
        draw.line(
            points,
            fill=(*color[:3], random.randint(75, 125)),
            width=random.randint(2, 4),
        )


def _draw_arcs(
    draw: ImageDraw.ImageDraw,
    width: int,
    height: int,
    palette: Sequence[tuple[int, int, int, int]],
    count: tuple[int, int],
) -> None:
    for _ in range(random.randint(*count)):
        margin = random.randint(20, 100)
        box = (
            random.randint(-margin, width // 3),
            random.randint(-height, height // 2),
            random.randint(width * 2 // 3, width + margin),
            random.randint(height // 2, height * 2),
        )
        color = random.choice(palette)
        draw.arc(
            box,
            start=random.randint(0, 120),
            end=random.randint(200, 355),
            fill=(*color[:3], random.randint(80, 135)),
            width=random.randint(2, 5),
        )


def _draw_cross_lines(
    draw: ImageDraw.ImageDraw,
    width: int,
    height: int,
    palette: Sequence[tuple[int, int, int, int]],
    count: tuple[int, int],
) -> None:
    for _ in range(random.randint(*count)):
        color = random.choice(palette)
        draw.line(
            (
                random.randint(0, width // 5),
                random.randint(0, height),
                random.randint(width * 4 // 5, width),
                random.randint(0, height),
            ),
            fill=(*color[:3], random.randint(55, 105)),
            width=random.randint(1, 3),
        )


def _draw_speckles(
    draw: ImageDraw.ImageDraw,
    width: int,
    height: int,
    density: float,
) -> None:
    for _ in range(int(width * height * density)):
        x = random.randrange(width)
        y = random.randrange(height)
        shade = random.randint(35, 190)
        radius = random.choice((1, 1, 1, 2))
        draw.ellipse((x, y, x + radius, y + radius), fill=(shade, shade, shade, random.randint(30, 100)))


def _text_palette(colors: Sequence[str] | None) -> list[tuple[int, int, int, int]]:
    if colors:
        probe = Image.new("RGB", (1, 1))
        probe_draw = ImageDraw.Draw(probe)
        parsed = []
        for color in colors:
            try:
                probe_draw.point((0, 0), fill=color)
                pixel = probe.getpixel((0, 0))
                if not isinstance(pixel, tuple) or len(pixel) < 3:
                    continue
                rgb = (int(pixel[0]), int(pixel[1]), int(pixel[2]))
                if max(rgb) - min(rgb) > 25 or max(rgb) < 150:
                    parsed.append((*rgb, 255))
            except (TypeError, ValueError):
                continue
        if parsed:
            return parsed
    return [
        (24, 51, 89, 255),
        (92, 37, 120, 255),
        (18, 92, 84, 255),
        (132, 45, 52, 255),
        (37, 45, 61, 255),
    ]


def _hsv_to_rgb(h: float, s: float, v: float) -> tuple[int, int, int]:
    import colorsys

    red, green, blue = colorsys.hsv_to_rgb(h, s, v)
    return int(red * 255), int(green * 255), int(blue * 255)
