from __future__ import annotations

import random

from PIL import ImageDraw

from CaptchaGenerator.core import (
    DEFAULT_COLORS as COLORS,
    ChallengeResult,
    VisualChallenge,
)
from CaptchaGenerator.core.renderer import create_background


class ColorChallengeCaptcha(VisualChallenge):
    def generate(self, *, name_export: str, path_export: str,
                 fonts: list[str]) -> ChallengeResult:
        word, ink = random.sample(list(COLORS), 2)
        image = create_background().resize((720, 300))
        draw, font = ImageDraw.Draw(image), self._load_font(fonts, 150)
        bbox = draw.textbbox((0, 0), word.upper(), font=font, stroke_width=2)
        x = (image.width - (bbox[2] - bbox[0])) // 2
        y = (image.height - (bbox[3] - bbox[1])) // 2 - bbox[1]
        draw.text((x, y), word.upper(), font=font, fill=COLORS[ink], stroke_width=2)
        return self._save(image, path_export=path_export, name_export=name_export,
                          answer=ink,
                          prompt="Enter the ink color, not the written word.",
                          metadata={"word": word, "ink_color": ink})
