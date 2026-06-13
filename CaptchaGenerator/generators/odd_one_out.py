from __future__ import annotations

import random

from PIL import ImageDraw

from CaptchaGenerator.exceptions import InvalidArgumentError
from CaptchaGenerator.core import (
    SHAPES,
    ChallengeResult,
    VisualChallenge,
    draw_shape,
    grid_positions,
)
from CaptchaGenerator.core.renderer import create_background


class OddOneOutCaptcha(VisualChallenge):
    def generate(self, *, name_export: str, path_export: str,
                 difficulty: str = "medium") -> ChallengeResult:
        side = {"easy": 3, "medium": 4, "hard": 5, "extreme": 6}.get(difficulty)
        if side is None:
            raise InvalidArgumentError("Unknown difficulty.")
        common = random.choice(SHAPES)
        odd = random.choice([shape for shape in SHAPES if shape != common])
        count, answer = side * side, random.randrange(side * side)
        image = create_background().resize((720, 420))
        draw = ImageDraw.Draw(image, "RGBA")
        for index, (x, y) in enumerate(grid_positions(count, *image.size, 55)):
            draw_shape(draw, odd if index == answer else common, x, y, 20,
                       (55, 90, 145))
        return self._save(image, path_export=path_export, name_export=name_export,
                          answer=answer, prompt="Select the different tile.",
                          metadata={"rows": side, "columns": side,
                                    "answer_is_zero_based": True})
