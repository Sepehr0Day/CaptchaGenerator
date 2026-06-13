from __future__ import annotations

import os
import random
from typing import TYPE_CHECKING, Any

from PIL import Image, ImageFont

if TYPE_CHECKING:
    from CaptchaGenerator.core.config import CaptchaConfig
    from PIL.Image import Image as PILImage
    from PIL.ImageFont import FreeTypeFont


class BaseCaptchaGenerator:
    """Shared services for all captcha generators."""

    def __init__(self, config: CaptchaConfig | None = None) -> None:
        from CaptchaGenerator.core.config import CaptchaConfig

        self.config = config or CaptchaConfig()
        if self.config.random_seed is not None:
            random.seed(self.config.random_seed)

    def _load_background(self, backgrounds: list[str]) -> PILImage:
        """Load a random background image or create a solid color one.

        Args:
            backgrounds: List of paths to background images.

        Returns:
            The loaded or generated PIL Image.
        """
        if backgrounds:
            for _ in range(len(backgrounds)):
                try:
                    path = random.choice(backgrounds)
                    if os.path.exists(path):
                        return Image.open(path).convert("RGBA")
                except Exception:
                    continue

        # Fallback: Create a random solid color background if no images found
        random_bg_color = (
            random.randint(20, 100),
            random.randint(20, 100),
            random.randint(20, 100),
            255
        )
        return Image.new("RGBA", self.config.size, color=random_bg_color)

    def _load_font(self, fonts: list[str], size: int) -> FreeTypeFont:
        """Load a random font at the specified size.

        Args:
            fonts: List of paths to font files.
            size: The font size to use.

        Returns:
            The loaded FreeTypeFont object or a fallback font.
        """
        # Try to load from the provided list
        font_sources = fonts or list(self.config.fonts)
        if font_sources:
            for _ in range(len(font_sources)):
                try:
                    path = random.choice(font_sources)
                    if os.path.exists(path):
                        return ImageFont.truetype(path, size)
                except Exception:
                    continue

        # Fallback 1: Common system fonts
        system_fonts = [
            "arial.ttf", "Roboto-Regular.ttf", "DejaVuSans.ttf", 
            "C:\\Windows\\Fonts\\arial.ttf", "C:\\Windows\\Fonts\\segoeui.ttf",
            "/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf",
            "/usr/share/fonts/TTF/DejaVuSans.ttf"
        ]
        for path in system_fonts:
            try:
                return ImageFont.truetype(path, size)
            except Exception:
                continue

        # Fallback 2: The basic built-in PIL font (Wrap it to support getbbox)
        default_font = ImageFont.load_default()
        
        # Add a mock getbbox to the default font if it doesn't have it
        if not hasattr(default_font, "getbbox"):
            def mock_getbbox(text: str) -> tuple[int, int, int, int]:
                # Default font is roughly 6x10 per char
                return (0, 0, len(text) * 6, 10)
            default_font.getbbox = mock_getbbox  # type: ignore

        return default_font  # type: ignore

    def _save_image(
        self,
        img: Image.Image,
        path: str,
        name: str,
        *,
        context: dict[str, Any] | None = None,
    ) -> str:
        """Save the captcha image to the specified path.

        Args:
            img: The PIL Image to save.
            path: The directory path to save in.
            name: The name of the file (without extension).

        Returns:
            The full output path of the saved image.
        """
        if not os.path.exists(path):
            os.makedirs(path, exist_ok=True)

        render_context = context or {}
        if self.config.pre_render_hook:
            img = self.config.pre_render_hook(img, render_context)
        if img.size != self.config.size:
            img = img.resize(self.config.size, Image.Resampling.LANCZOS)
        if self.config.post_render_hook:
            img = self.config.post_render_hook(img, render_context)
        full_path = os.path.join(path, f"{name}.{self.config.extension}")
        save_kwargs: dict[str, Any] = {}
        if self.config.output_format.upper() in {"JPEG", "JPG", "WEBP"}:
            save_kwargs["quality"] = self.config.quality
        if self.config.output_format.upper() in {"JPEG", "JPG"}:
            img = img.convert("RGB")
        img.save(full_path, format=self.config.output_format, **save_kwargs)
        return full_path
