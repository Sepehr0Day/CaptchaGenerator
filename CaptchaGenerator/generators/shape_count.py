from __future__ import annotations

import random

from PIL import ImageDraw

from CaptchaGenerator.exceptions import InvalidArgumentError
from CaptchaGenerator.core import (
    DEFAULT_COLORS as COLORS,
    SHAPES,
    ChallengeResult,
    VisualChallenge,
    draw_shape,
    grid_positions,
)
from CaptchaGenerator.core.renderer import create_background


class ShapeCountCaptcha(VisualChallenge):
    def generate(self, *, name_export: str, path_export: str, fonts: list[str],
                 difficulty: str = "medium") -> ChallengeResult:
        total = {"easy": 8, "medium": 14, "hard": 22, "extreme": 30}.get(difficulty)
        if total is None:
            raise InvalidArgumentError("Unknown difficulty.")
        target = random.choice(SHAPES)
        items = [random.choice(SHAPES) for _ in range(total - 2)] + [target, target]
        random.shuffle(items)
        image = create_background().resize((720, 420))
        draw = ImageDraw.Draw(image, "RGBA")
        for shape, (x, y) in zip(items, grid_positions(total, *image.size, 65)):
            draw_shape(draw, shape, x, y, random.randint(20, 30),
                       random.choice(list(COLORS.values())))
        return self._save(image, path_export=path_export, name_export=name_export,
                          answer=items.count(target),
                          prompt=f"How many {target}s are shown?",
                          metadata={"target": target, "total_shapes": total})
