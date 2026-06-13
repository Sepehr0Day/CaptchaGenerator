from __future__ import annotations

import random

from CaptchaGenerator.exceptions import InvalidArgumentError
from CaptchaGenerator.core import ChallengeResult, VisualChallenge
from CaptchaGenerator.core.renderer import render_captcha


class MathImageCaptcha(VisualChallenge):
    def generate(self, *, name_export: str, path_export: str, fonts: list[str],
                 difficulty: str = "medium", style: str = "modern") -> ChallengeResult:
        maximum = {"easy": 10, "medium": 20, "hard": 50, "extreme": 99}.get(difficulty)
        if maximum is None:
            raise InvalidArgumentError("Unknown difficulty.")
        left, right = random.randint(1, maximum), random.randint(1, maximum)
        operator = random.choice(("+", "-", "*"))
        if operator == "-" and right > left:
            left, right = right, left
        answer = {"+": left + right, "-": left - right, "*": left * right}[operator]
        expression = f"{left} {operator} {right}"
        image = render_captcha(expression, font_loader=self._load_font, fonts=fonts,
                               difficulty=difficulty, style=style)
        return self._save(image, path_export=path_export, name_export=name_export,
                          answer=answer, prompt="Solve the expression.",
                          metadata={"expression": expression})
