from __future__ import annotations

from collections.abc import Callable, Sequence

from PIL import Image, ImageDraw, ImageFont

from CaptchaGenerator.core import CaptchaConfig, ChallengeResult, VisualChallenge
from CaptchaGenerator.exceptions import InvalidArgumentError

QuestionProvider = Callable[[], tuple[str, object]]


class CustomQuestionCaptcha(VisualChallenge):
    """Render developer-provided questions and answers."""

    def generate(
        self,
        *,
        name_export: str,
        path_export: str,
        question: str | None = None,
        answer: object | None = None,
        questions: Sequence[tuple[str, object]] | None = None,
        provider: QuestionProvider | None = None,
        config: CaptchaConfig | None = None,
    ) -> ChallengeResult:
        import random

        if provider:
            question, answer = provider()
        elif questions:
            question, answer = random.choice(list(questions))
        if not question or answer is None:
            raise InvalidArgumentError(
                "Provide question+answer, questions, or a provider."
            )
        resolved = self._config(config)
        image = Image.new("RGB", resolved.size, resolved.background_color)
        draw = ImageDraw.Draw(image)
        font = self._load_font(
            list(resolved.fonts), resolved.font_size or max(22, resolved.height // 8)
        )
        lines = wrap_text(draw, question, font, resolved.width - resolved.padding * 2)
        y = (resolved.height - len(lines) * (font.size + 8)) // 2
        for line in lines:
            box = draw.textbbox((0, 0), line, font=font)
            draw.text(((resolved.width - (box[2] - box[0])) // 2, y),
                      line, font=font, fill=resolved.foreground_color)
            y += font.size + 8
        return self._save(
            image, path_export=path_export, name_export=name_export,
            answer=answer, prompt=question,
            metadata={"question": question, "answer_type": type(answer).__name__},
            config=resolved,
        )


def wrap_text(draw: ImageDraw.ImageDraw, text: str, font: ImageFont.FreeTypeFont,
              maximum_width: int) -> list[str]:
    lines, current = [], ""
    for word in text.split():
        candidate = f"{current} {word}".strip()
        if draw.textbbox((0, 0), candidate, font=font)[2] <= maximum_width:
            current = candidate
        else:
            if current:
                lines.append(current)
            current = word
    if current:
        lines.append(current)
    return lines
