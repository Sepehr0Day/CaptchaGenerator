from __future__ import annotations

import math

from PIL import Image, ImageDraw

from CaptchaGenerator.core.config import Color


def grid_positions(
    count: int, width: int, height: int, margin: int
) -> list[tuple[int, int]]:
    columns = math.ceil(math.sqrt(count * width / height))
    rows = math.ceil(count / columns)
    cell_width = (width - margin * 2) / columns
    cell_height = (height - margin * 2) / rows
    return [
        (
            int(margin + (index % columns + 0.5) * cell_width),
            int(margin + (index // columns + 0.5) * cell_height),
        )
        for index in range(count)
    ]


def regular_polygon(
    center: tuple[float, float], radius: float, sides: int, rotation: float = 0
) -> list[tuple[float, float]]:
    return [
        (
            center[0] + math.cos(rotation + index * math.tau / sides) * radius,
            center[1] + math.sin(rotation + index * math.tau / sides) * radius,
        )
        for index in range(sides)
    ]


def draw_shape(
    draw: ImageDraw.ImageDraw,
    shape: str,
    x: int,
    y: int,
    size: int,
    color: Color,
    *,
    outline: Color = (25, 35, 50, 230),
    line_width: int = 3,
) -> None:
    box = (x - size, y - size, x + size, y + size)
    if shape == "circle":
        draw.ellipse(box, fill=color, outline=outline, width=line_width)
    elif shape == "square":
        draw.rounded_rectangle(
            box, radius=max(2, size // 5), fill=color, outline=outline,
            width=line_width
        )
    elif shape == "triangle":
        draw.polygon(
            ((x, y - size), (x - size, y + size), (x + size, y + size)),
            fill=color, outline=outline
        )
    else:
        draw.polygon(
            ((x, y - size), (x - size, y), (x, y + size), (x + size, y)),
            fill=color, outline=outline
        )


def fit_image(source: Image.Image, size: tuple[int, int]) -> Image.Image:
    image = source.convert("RGB")
    image.thumbnail(size, Image.Resampling.LANCZOS)
    canvas = Image.new("RGB", size, "white")
    canvas.paste(
        image, ((size[0] - image.width) // 2, (size[1] - image.height) // 2)
    )
    return canvas
