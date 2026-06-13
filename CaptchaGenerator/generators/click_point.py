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


class ClickPointCaptcha(VisualChallenge):
    def generate(self, *, name_export: str, path_export: str,
                 target: str | None = None) -> ChallengeResult:
        target = target or random.choice(SHAPES)
        if target not in SHAPES:
            raise InvalidArgumentError(f"target must be one of: {', '.join(SHAPES)}")
        image = create_background().resize((720, 420))
        draw = ImageDraw.Draw(image, "RGBA")
        positions = grid_positions(10, *image.size, 75)
        chosen_index = random.randrange(len(positions))
        alternatives = [shape for shape in SHAPES if shape != target]
        for index, (x, y) in enumerate(positions):
            shape = target if index == chosen_index else random.choice(alternatives)
            draw_shape(draw, shape, x, y, 28, random.choice(list(COLORS.values())))
        x, y = positions[chosen_index]
        return self._save(image, path_export=path_export, name_export=name_export,
                          answer=(x, y), prompt=f"Click the center of the {target}.",
                          metadata={"target": target, "tolerance": 35})
