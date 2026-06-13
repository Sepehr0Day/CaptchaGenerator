from __future__ import annotations

from CaptchaGenerator.base import BaseCaptchaGenerator
from CaptchaGenerator.exceptions import InvalidArgumentError
from CaptchaGenerator.core.renderer import render_captcha, validate_text_request


class TextCaptcha(BaseCaptchaGenerator):
    """Generator for standard text-based captchas."""

    def generate(
        self,
        *,
        number_gen: int,
        values_captcha: str,
        name_export: str,
        path_export: str,
        fonts: list[str],
        colors: list[str],
        backgrounds: list[str],
        difficulty: str = "medium",
        style: str = "modern",
    ) -> str:
        """Generate a text captcha image and return the correct answer.

        Args:
            number_gen: Number of characters to generate.
            values_captcha: String containing possible characters.
            name_export: Filename for the exported image.
            path_export: Directory path for the exported image.
            fonts: List of font file paths.
            colors: List of color names to use for the text.
            backgrounds: List of background image paths.

        Returns:
            The correct answer string that was rendered.

        Raises:
            InvalidArgumentError: If any required argument is missing or invalid.
        """
        import random

        validate_text_request(length=int(number_gen), values=values_captcha, fonts=fonts)
        if not colors:
            raise InvalidArgumentError("colors must contain at least one color.")
        choice_from_values = "".join(
            random.choice(values_captcha) for _ in range(int(number_gen))
        )
        background = self._load_background(backgrounds) if backgrounds else None
        img = render_captcha(
            choice_from_values,
            font_loader=self._load_font,
            fonts=fonts,
            background=background,
            preferred_colors=colors,
            difficulty=difficulty,
            style=style,
        )
        self._save_image(img, path_export, name_export)
        return choice_from_values
