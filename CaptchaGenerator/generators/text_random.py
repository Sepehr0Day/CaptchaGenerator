from __future__ import annotations

import random

from CaptchaGenerator.base import BaseCaptchaGenerator
from CaptchaGenerator.exceptions import InvalidArgumentError
from CaptchaGenerator.core.renderer import render_captcha, validate_text_request


class TextRandomCaptcha(BaseCaptchaGenerator):
    """Generator for text captchas with multiple random variants."""

    def generate(
        self,
        *,
        number_gen: int,
        values_captcha: str,
        number_variants: int,
        backgrounds: list[str],
        fonts: list[str],
        name_export: str,
        path_export: str,
        difficulty: str = "medium",
        style: str = "modern",
    ) -> tuple[str, list[str]]:
        """Generate a random text captcha and return the answer and variants.

        Args:
            number_gen: Number of characters per variant.
            values_captcha: String of possible characters.
            number_variants: Number of total variants to generate.
            backgrounds: List of background image paths.
            fonts: List of font file paths.
            name_export: Filename for the exported image.
            path_export: Directory path for the exported image.

        Returns:
            A tuple containing (correct_answer, all_variants).
        """
        validate_text_request(length=int(number_gen), values=values_captcha, fonts=fonts)
        if number_variants <= 0:
            raise InvalidArgumentError("number_variants must be greater than zero.")
        variants = [
            "".join(random.choice(values_captcha) for _ in range(number_gen))
            for _ in range(number_variants)
        ]
        correct_answer = random.choice(variants)
        background = self._load_background(backgrounds) if backgrounds else None
        img = render_captcha(
            correct_answer,
            font_loader=self._load_font,
            fonts=fonts,
            background=background,
            difficulty=difficulty,
            style=style,
        )
        self._save_image(img, path_export, name_export)
        return correct_answer, variants
