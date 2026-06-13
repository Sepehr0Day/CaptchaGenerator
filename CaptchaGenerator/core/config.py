from __future__ import annotations

from dataclasses import dataclass, field
from typing import Any, Callable

from PIL import Image

Color = str | tuple[int, int, int] | tuple[int, int, int, int]
ImageHook = Callable[[Image.Image, dict[str, Any]], Image.Image]


@dataclass(frozen=True)
class CaptchaConfig:
    """Shared customization options accepted by visual captcha generators."""

    width: int = 720
    height: int = 240
    output_format: str = "PNG"
    quality: int = 92
    background_color: Color = (240, 244, 250)
    foreground_color: Color = (35, 45, 65)
    accent_colors: tuple[Color, ...] = (
        (205, 55, 65),
        (45, 105, 190),
        (45, 145, 90),
        (225, 125, 40),
        (130, 75, 175),
    )
    fonts: tuple[str, ...] = ()
    font_size: int | None = None
    line_width: int = 3
    padding: int = 24
    language: str = "en"
    prompt: str | None = None
    accessibility_text: str | None = None
    high_contrast: bool = False
    include_answer_in_metadata: bool = False
    random_seed: int | None = None
    pre_render_hook: ImageHook | None = field(default=None, repr=False)
    post_render_hook: ImageHook | None = field(default=None, repr=False)

    @property
    def size(self) -> tuple[int, int]:
        return self.width, self.height

    @property
    def extension(self) -> str:
        return {"JPEG": "jpg", "JPG": "jpg", "GIF": "gif"}.get(
            self.output_format.upper(), self.output_format.lower()
        )
