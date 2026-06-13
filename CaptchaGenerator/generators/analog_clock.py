from __future__ import annotations

import math
import random

from PIL import Image, ImageDraw

from CaptchaGenerator.core import CaptchaConfig, ChallengeResult, Color, VisualChallenge


class AnalogClockCaptcha(VisualChallenge):
    """Read a randomly generated analog clock."""

    def generate(
        self,
        *,
        name_export: str,
        path_export: str,
        minute_step: int = 5,
        show_numbers: bool = True,
        twenty_four_hour_answer: bool = False,
        config: CaptchaConfig | None = None,
    ) -> ChallengeResult:
        resolved = self._config(config)
        hour = random.randint(1, 12)
        minute = random.randrange(0, 60, minute_step)
        image = Image.new("RGB", resolved.size, resolved.background_color)
        draw = ImageDraw.Draw(image)
        radius = min(resolved.width, resolved.height) // 2 - resolved.padding * 2
        center = (resolved.width // 2, resolved.height // 2)
        draw.ellipse(
            (center[0] - radius, center[1] - radius,
             center[0] + radius, center[1] + radius),
            fill="white",
            outline=resolved.foreground_color,
            width=resolved.line_width + 1,
        )
        font = self._load_font(list(resolved.fonts), max(14, radius // 8))
        for value in range(1, 13):
            angle = math.radians(value * 30 - 90)
            outer = (
                center[0] + math.cos(angle) * radius * 0.9,
                center[1] + math.sin(angle) * radius * 0.9,
            )
            inner = (
                center[0] + math.cos(angle) * radius * 0.82,
                center[1] + math.sin(angle) * radius * 0.82,
            )
            draw.line((inner, outer), fill=resolved.foreground_color,
                      width=resolved.line_width)
            if show_numbers:
                text = str(value)
                box = draw.textbbox((0, 0), text, font=font)
                x = center[0] + math.cos(angle) * radius * 0.69
                y = center[1] + math.sin(angle) * radius * 0.69
                draw.text((x - (box[2] - box[0]) / 2,
                           y - (box[3] - box[1]) / 2 - box[1]),
                          text, font=font, fill=resolved.foreground_color)
        hour_angle = math.radians((hour % 12 + minute / 60) * 30 - 90)
        minute_angle = math.radians(minute * 6 - 90)
        self._hand(draw, center, radius * 0.50, hour_angle,
                   resolved.foreground_color, resolved.line_width + 5)
        self._hand(draw, center, radius * 0.72, minute_angle,
                   resolved.accent_colors[0], resolved.line_width + 2)
        draw.ellipse((center[0] - 7, center[1] - 7, center[0] + 7,
                      center[1] + 7), fill=resolved.foreground_color)
        answer_hour = hour if not twenty_four_hour_answer else hour % 24
        answer = f"{answer_hour:02d}:{minute:02d}"
        return self._save(
            image, path_export=path_export, name_export=name_export,
            answer=answer, prompt="Enter the time shown on the clock.",
            metadata={"hour": hour, "minute": minute, "minute_step": minute_step},
            config=resolved,
        )

    @staticmethod
    def _hand(draw: ImageDraw.ImageDraw, center: tuple[int, int], length: float,
              angle: float, color: Color, width: int) -> None:
        end = (center[0] + math.cos(angle) * length,
               center[1] + math.sin(angle) * length)
        draw.line((center, end), fill=color, width=width)
