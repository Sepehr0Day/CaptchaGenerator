from __future__ import annotations

import os
import random
from pathlib import Path

from PIL import Image, ImageDraw, ImageFilter

from CaptchaGenerator.core import (
    CaptchaConfig,
    ChallengeResult,
    VisualChallenge,
)
from CaptchaGenerator.exceptions import InvalidArgumentError


class IrregularPuzzleCaptcha(VisualChallenge):
    """Slider puzzle with a non-rectangular missing piece."""

    def generate(
        self,
        *,
        image_path: str | None = None,
        name_export: str,
        path_export: str,
        vertices: int = 8,
        piece_radius: int | None = None,
        tolerance: int = 8,
        config: CaptchaConfig | None = None,
    ) -> ChallengeResult:
        if image_path is not None and not os.path.exists(image_path):
            raise InvalidArgumentError(f"Image not found: {image_path}")
        if vertices < 5:
            raise InvalidArgumentError("vertices must be at least 5.")
        resolved = self._config(config)
        image = (
            Image.open(image_path).convert("RGB").resize(resolved.size)
            if image_path
            else procedural_puzzle_background(resolved)
        )
        radius = piece_radius or max(28, min(resolved.size) // 9)
        target_x = random.randint(radius * 3, resolved.width - radius * 2)
        target_y = random.randint(radius * 2, resolved.height - radius * 2)
        angles = sorted(random.random() * 6.283 for _ in range(vertices))
        local_points = [
            (
                radius + math_cos(angle) * radius * random.uniform(0.72, 1.0),
                radius + math_sin(angle) * radius * random.uniform(0.72, 1.0),
            )
            for angle in angles
        ]
        mask = Image.new("L", (radius * 2, radius * 2), 0)
        ImageDraw.Draw(mask).polygon(local_points, fill=255)
        crop = image.crop(
            (target_x - radius, target_y - radius,
             target_x + radius, target_y + radius)
        )
        piece = Image.new("RGBA", crop.size, (0, 0, 0, 0))
        piece.paste(crop, (0, 0), mask)
        shadow = mask.filter(ImageFilter.GaussianBlur(4))
        overlay = Image.new("RGBA", image.size, (0, 0, 0, 0))
        overlay.paste((20, 25, 35, 210), (target_x - radius, target_y - radius),
                      shadow)
        image = Image.alpha_composite(image.convert("RGBA"), overlay)
        background = image.copy()
        start_x = resolved.padding + radius
        image.alpha_composite(piece, (start_x - radius, target_y - radius))
        draw = ImageDraw.Draw(image)
        target_points = [
            (target_x - radius + x, target_y - radius + y)
            for x, y in local_points
        ]
        draw.line(target_points + [target_points[0]], fill="white",
                  width=resolved.line_width)
        output = Path(path_export)
        output.mkdir(parents=True, exist_ok=True)
        background_path = output / f"{name_export}_background.png"
        piece_path = output / f"{name_export}_piece.png"
        background.convert("RGB").save(background_path)
        piece.save(piece_path)
        return self._save(
            image.convert("RGB"), path_export=path_export,
            name_export=name_export, answer=target_x,
            prompt="Move the irregular piece into the matching hole.",
            metadata={
                "piece_start_x": start_x,
                "target_x": target_x,
                "target_y": target_y,
                "tolerance": tolerance,
                "mask_points": local_points,
                "piece_radius": radius,
                "background_path": str(background_path),
                "piece_path": str(piece_path),
            },
            config=resolved,
        )


def math_cos(value: float) -> float:
    import math
    return math.cos(value)


def math_sin(value: float) -> float:
    import math
    return math.sin(value)


def procedural_puzzle_background(config: CaptchaConfig) -> Image.Image:
    image = Image.new("RGB", config.size, config.background_color)
    draw = ImageDraw.Draw(image)
    colors = list(config.accent_colors)
    band = max(20, config.width // 12)
    for index, x in enumerate(range(-config.height, config.width, band)):
        draw.polygon(
            ((x, 0), (x + band, 0), (x + config.height + band, config.height),
             (x + config.height, config.height)),
            fill=colors[index % len(colors)],
        )
    for _ in range(18):
        x, y = random.randrange(config.width), random.randrange(config.height)
        radius = random.randint(8, 28)
        draw.ellipse((x - radius, y - radius, x + radius, y + radius),
                     outline="white", width=2)
    return image
