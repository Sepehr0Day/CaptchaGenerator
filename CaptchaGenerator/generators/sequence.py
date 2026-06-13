from __future__ import annotations

import random

from PIL import Image, ImageDraw

from CaptchaGenerator.exceptions import InvalidArgumentError
from CaptchaGenerator.core import ChallengeResult, VisualChallenge


class SequenceCaptcha(VisualChallenge):
    def generate(self, *, name_export: str, path_export: str, fonts: list[str],
                 difficulty: str = "medium", style: str = "minimal") -> ChallengeResult:
        count = {"easy": 4, "medium": 5, "hard": 6, "extreme": 6}.get(difficulty)
        if count is None:
            raise InvalidArgumentError("Unknown difficulty.")
        rule_value: int
        if difficulty in {"hard", "extreme"} and random.choice((True, False)):
            start, ratio = random.randint(1, 5), random.randint(2, 3)
            sequence = [start * ratio**index for index in range(count)]
            answer, rule = sequence[-1] * ratio, "geometric"
            rule_value = ratio
        else:
            start = random.randint(1, 20)
            step = random.randint(1, 5 if difficulty == "easy" else 12)
            sequence = [start + step * index for index in range(count)]
            answer, rule = sequence[-1] + step, "arithmetic"
            rule_value = step

        resolved = self._config(None)
        image = Image.new("RGB", resolved.size, resolved.background_color)
        draw = ImageDraw.Draw(image)
        text = "  •  ".join(map(str, sequence)) + "  •  ?"
        maximum_width = resolved.width - resolved.padding * 2
        font_size = resolved.font_size or max(28, resolved.height // 4)
        font = self._load_font(fonts, font_size)
        while (
            draw.textbbox((0, 0), text, font=font)[2] > maximum_width
            and font_size > 18
        ):
            font_size -= 2
            font = self._load_font(fonts, font_size)
        box = draw.textbbox((0, 0), text, font=font)
        text_width = box[2] - box[0]
        text_height = box[3] - box[1]
        x = (resolved.width - text_width) // 2
        y = (resolved.height - text_height) // 2 - box[1]
        draw.rounded_rectangle(
            (
                resolved.padding,
                resolved.padding,
                resolved.width - resolved.padding,
                resolved.height - resolved.padding,
            ),
            radius=18,
            fill="white",
            outline=resolved.accent_colors[0],
            width=resolved.line_width,
        )
        draw.text((x, y), text, font=font, fill=resolved.foreground_color)
        return self._save(image, path_export=path_export, name_export=name_export,
                          answer=answer, prompt="Enter the next number.",
                          metadata={
                              "sequence": sequence,
                              "rule": rule,
                              "rule_value": rule_value,
                              "style": style,
                          },
                          config=resolved)
