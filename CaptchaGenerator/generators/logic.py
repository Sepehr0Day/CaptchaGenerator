from __future__ import annotations

import random

from PIL import Image, ImageDraw

from CaptchaGenerator.core import ChallengeResult, VisualChallenge


class LogicChallengeCaptcha(VisualChallenge):
    def generate(self, *, name_export: str, path_export: str, fonts: list[str],
                 difficulty: str = "medium") -> ChallengeResult:
        mode = random.choice(("comparison", "parity", "sum"))
        if mode == "comparison":
            numbers = random.sample(range(1, 30), 3)
            answer = max(numbers)
            question = f"Which number is largest?  {'   '.join(map(str, numbers))}"
        elif mode == "parity":
            numbers = [random.randrange(2, 30, 2) for _ in range(3)]
            answer = random.randrange(1, 30, 2)
            numbers.insert(random.randrange(4), answer)
            question = f"Which number is odd?  {'   '.join(map(str, numbers))}"
        else:
            left, right = random.randint(1, 15), random.randint(1, 15)
            answer = left + right
            options = list({answer, answer + 1, max(0, answer - 2), answer + 3})
            while len(options) < 4:
                options.append(answer + len(options))
            random.shuffle(options)
            question = f"{left} + {right} = ?   Options: {' / '.join(map(str, options))}"
        image, draw = Image.new("RGB", (900, 300), (240, 244, 250)), None
        draw = ImageDraw.Draw(image)
        font_size = 54
        while font_size >= 24:
            font = self._load_font(fonts, font_size)
            bbox = draw.textbbox((0, 0), question, font=font)
            if bbox[2] - bbox[0] <= image.width - 70:
                break
            font_size -= 2
        width, height = bbox[2] - bbox[0], bbox[3] - bbox[1]
        draw.text(((image.width - width) // 2,
                   (image.height - height) // 2 - bbox[1]), question,
                  font=font, fill=(35, 45, 65))
        return self._save(image, path_export=path_export, name_export=name_export,
                          answer=answer, prompt="Answer the visual logic question.",
                          metadata={"mode": mode, "question": question})
