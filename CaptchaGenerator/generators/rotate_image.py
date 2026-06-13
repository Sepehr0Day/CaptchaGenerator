from __future__ import annotations

import os
import random

from PIL import Image

from CaptchaGenerator.exceptions import InvalidArgumentError
from CaptchaGenerator.core import ChallengeResult, VisualChallenge


class RotateImageCaptcha(VisualChallenge):
    def generate(self, *, image_path: str, name_export: str,
                 path_export: str) -> ChallengeResult:
        if not os.path.exists(image_path):
            raise InvalidArgumentError(f"Image not found: {image_path}")
        angle = random.choice((90, 180, 270))
        source = Image.open(image_path).convert("RGB")
        source.thumbnail((520, 320))
        rotated = source.rotate(angle, expand=True, fillcolor=(235, 240, 247))
        canvas = Image.new("RGB", (720, 420), (235, 240, 247))
        canvas.paste(rotated, ((canvas.width - rotated.width) // 2,
                               (canvas.height - rotated.height) // 2))
        return self._save(canvas, path_export=path_export, name_export=name_export,
                          answer={
                              90: "clockwise",
                              180: "180",
                              270: "counterclockwise",
                          }[angle],
                          prompt="How should the image be rotated to become upright?",
                          metadata={
                              "applied_rotation_degrees": angle,
                              "rotation_direction": "counterclockwise",
                              "answer_options": (
                                  "clockwise",
                                  "counterclockwise",
                                  "180",
                              ),
                          })
