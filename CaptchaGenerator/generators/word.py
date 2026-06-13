from __future__ import annotations

from CaptchaGenerator.base import BaseCaptchaGenerator
from CaptchaGenerator.exceptions import InvalidArgumentError
from CaptchaGenerator.core.renderer import render_captcha


class WordCaptcha(BaseCaptchaGenerator):
    """Generator for word-based captchas using a dictionary file."""

    def generate(
        self,
        *,
        backgrounds: list[str],
        path_words: str,
        fonts: list[str],
        font_size: int,
        name_export: str,
        path_export: str,
        difficulty: str = "medium",
        style: str = "modern",
    ) -> str:
        """Generate a word captcha image from a words file.

        Args:
            backgrounds: List of background image paths.
            path_words: Path to the text file containing words (one per line).
            fonts: List of font file paths.
            font_size: Size of the font to use.
            name_export: Filename for the exported image.
            path_export: Directory path for the exported image.

        Returns:
            The word that was rendered.

        Raises:
            InvalidArgumentError: If the words file is missing or empty.
        """
        import random

        if font_size <= 0:
            raise InvalidArgumentError("font_size must be greater than zero.")
        with open(path_words, "r", encoding="utf-8") as f:
            words = [line.strip() for line in f if line.strip()]
        if not words:
            raise InvalidArgumentError("Words file is empty.")

        correct_answer = random.choice(words)
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
        return correct_answer
