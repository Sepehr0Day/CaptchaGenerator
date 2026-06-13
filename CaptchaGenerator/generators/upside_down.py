from __future__ import annotations

import os
import random
import math

from PIL import Image, ImageDraw

from CaptchaGenerator.core import (
    CaptchaConfig,
    ChallengeResult,
    Color,
    VisualChallenge,
    grid_positions,
)
from CaptchaGenerator.exceptions import InvalidArgumentError


class UpsideDownObjectCaptcha(VisualChallenge):
    """Find the single upside-down object in a configurable grid."""

    def generate(
        self,
        *,
        name_export: str,
        path_export: str,
        image_path: str | None = None,
        item_count: int = 9,
        rotation: int = 180,
        config: CaptchaConfig | None = None,
    ) -> ChallengeResult:
        if image_path is not None and not os.path.exists(image_path):
            raise InvalidArgumentError(f"Image not found: {image_path}")
        if item_count < 4:
            raise InvalidArgumentError("item_count must be at least 4.")
        resolved = self._config(config)
        image = Image.new("RGB", resolved.size, resolved.background_color)
        source = (
            Image.open(image_path).convert("RGBA")
            if image_path
            else create_arrow_icon(
                max(72, min(resolved.width, resolved.height) // 4),
                resolved.accent_colors[0],
                resolved.foreground_color,
            )
        )
        cell = int(min(resolved.width, resolved.height) / math_grid(item_count) * 0.55)
        source.thumbnail((cell, cell))
        positions = grid_positions(
            item_count, resolved.width, resolved.height, resolved.padding + cell // 2
        )
        answer = random.randrange(item_count)
        draw = ImageDraw.Draw(image)
        for index, (x, y) in enumerate(positions):
            tile = source.rotate(rotation, expand=True) if index == answer else source
            image.paste(tile, (x - tile.width // 2, y - tile.height // 2), tile)
            draw.text((x - 8, y + cell // 2), str(index + 1),
                      fill=resolved.foreground_color)
        return self._save(
            image, path_export=path_export, name_export=name_export,
            answer=answer, prompt="Select the upside-down object.",
            metadata={"item_count": item_count, "answer_is_zero_based": True,
                      "rotation": rotation},
            config=resolved,
        )


def math_grid(count: int) -> int:
    return max(2, math.ceil(math.sqrt(count)))


def create_arrow_icon(size: int, fill: Color, outline: Color) -> Image.Image:
    icon = Image.new("RGBA", (size, size), (0, 0, 0, 0))
    draw = ImageDraw.Draw(icon)
    points = [
        (size * 0.5, size * 0.08),
        (size * 0.86, size * 0.45),
        (size * 0.65, size * 0.45),
        (size * 0.65, size * 0.9),
        (size * 0.35, size * 0.9),
        (size * 0.35, size * 0.45),
        (size * 0.14, size * 0.45),
    ]
    draw.polygon(points, fill=fill, outline=outline)
    return icon
