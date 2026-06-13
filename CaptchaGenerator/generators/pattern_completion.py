from __future__ import annotations

import random

from PIL import Image, ImageDraw

from CaptchaGenerator.core import (
    SHAPES,
    CaptchaConfig,
    ChallengeResult,
    VisualChallenge,
    draw_shape,
)


class PatternCompletionCaptcha(VisualChallenge):
    """Choose the shape that completes a visual repeating pattern."""

    def generate(
        self,
        *,
        name_export: str,
        path_export: str,
        pattern_length: int = 7,
        option_count: int = 4,
        config: CaptchaConfig | None = None,
    ) -> ChallengeResult:
        resolved = self._config(config)
        cycle_length = random.choice((2, 3))
        cycle = random.sample(SHAPES, cycle_length)
        pattern = [cycle[index % cycle_length] for index in range(pattern_length)]
        missing_index = random.randrange(1, pattern_length)
        answer_shape = pattern[missing_index]
        visible = pattern.copy()
        visible[missing_index] = "missing"
        options = [answer_shape]
        while len(options) < min(option_count, len(SHAPES)):
            candidate = random.choice(SHAPES)
            if candidate not in options:
                options.append(candidate)
        random.shuffle(options)
        answer = options.index(answer_shape)
        image = Image.new("RGB", resolved.size, resolved.background_color)
        draw = ImageDraw.Draw(image, "RGBA")
        shape_color = resolved.accent_colors[0]
        usable_width = resolved.width - resolved.padding * 2
        spacing = usable_width / pattern_length
        y = resolved.height * 0.36
        size = int(min(spacing * 0.32, resolved.height * 0.1))
        for index, shape in enumerate(visible):
            x = int(resolved.padding + spacing * (index + 0.5))
            if shape == "missing":
                draw.rounded_rectangle(
                    (x - size, y - size, x + size, y + size),
                    radius=5, outline=resolved.foreground_color,
                    width=resolved.line_width
                )
                draw.text((x - 5, y - 10), "?", fill=resolved.foreground_color)
            else:
                draw_shape(draw, shape, x, int(y), size,
                           shape_color,
                           line_width=resolved.line_width)
        option_y = int(resolved.height * 0.72)
        option_spacing = usable_width / len(options)
        for index, shape in enumerate(options):
            x = int(resolved.padding + option_spacing * (index + 0.5))
            draw_shape(draw, shape, x, option_y, size,
                       shape_color,
                       line_width=resolved.line_width)
            draw.text((x - 5, option_y + size + 8), str(index + 1),
                      fill=resolved.foreground_color)
        return self._save(
            image, path_export=path_export, name_export=name_export,
            answer=answer, prompt="Select the shape that completes the pattern.",
            metadata={
                "pattern": pattern,
                "missing_index": missing_index,
                "options": options,
                "answer_is_zero_based": True,
            },
            config=resolved,
        )
