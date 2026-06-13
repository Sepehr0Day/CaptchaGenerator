from __future__ import annotations

import random
from collections.abc import Sequence

from CaptchaGenerator.exceptions import InvalidArgumentError
from CaptchaGenerator.core import ChallengeResult, VisualChallenge
from CaptchaGenerator.core.renderer import render_captcha


class MissingCharacterCaptcha(VisualChallenge):
    def generate(self, *, name_export: str, path_export: str, fonts: list[str],
                 values: str = "ABCDEFGHJKLMNPQRSTUVWXYZ23456789", length: int = 6,
                 difficulty: str = "medium", style: str = "modern",
                 word: str | None = None,
                 words: Sequence[str] | None = None,
                 random_mode: bool = False) -> ChallengeResult:
        if random_mode:
            if length < 3 or not values:
                raise InvalidArgumentError(
                    "length must be at least 3 and values non-empty."
                )
            original = "".join(random.choice(values) for _ in range(length))
            source = "random"
        else:
            candidates = list(words or (
                "APPLE", "BANANA", "ORANGE", "PLANET", "GARDEN",
                "WINDOW", "PURPLE", "SCHOOL", "BRIDGE", "CAMERA",
            ))
            original = (word or random.choice(candidates)).strip().upper()
            if len(original) < 3:
                raise InvalidArgumentError("word must contain at least 3 characters.")
            source = "word"
        index = random.randrange(length if random_mode else len(original))
        puzzle = f"{original[:index]}?{original[index + 1:]}"
        image = render_captcha(puzzle, font_loader=self._load_font, fonts=fonts,
                               difficulty=difficulty, style=style)
        return self._save(image, path_export=path_export, name_export=name_export,
                          answer=original[index], prompt="Enter the missing character.",
                          metadata={"index": index, "puzzle": puzzle,
                                    "source": source,
                                    "word_length": len(original)})
