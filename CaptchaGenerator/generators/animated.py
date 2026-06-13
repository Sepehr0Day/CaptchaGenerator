from __future__ import annotations

import os
import random

from CaptchaGenerator.exceptions import InvalidArgumentError
from CaptchaGenerator.core import ChallengeResult, VisualChallenge
from CaptchaGenerator.core.renderer import render_captcha


class AnimatedCaptcha(VisualChallenge):
    def generate(self, *, name_export: str, path_export: str, fonts: list[str],
                 values: str = "ABCDEFGHJKLMNPQRSTUVWXYZ23456789", length: int = 6,
                 difficulty: str = "medium", style: str = "modern",
                 frame_count: int = 8) -> ChallengeResult:
        if frame_count < 2:
            raise InvalidArgumentError("frame_count must be at least 2.")
        answer = "".join(random.choice(values) for _ in range(length))
        frames = [render_captcha(answer, font_loader=self._load_font, fonts=fonts,
                                 difficulty=difficulty, style=style)
                  for _ in range(frame_count)]
        os.makedirs(path_export, exist_ok=True)
        path = os.path.join(path_export, f"{name_export}.gif")
        frames[0].save(path, save_all=True, append_images=frames[1:],
                       duration=120, loop=0, optimize=True)
        return ChallengeResult(answer, path, "Enter the animated characters.",
                               {"frame_count": frame_count})
