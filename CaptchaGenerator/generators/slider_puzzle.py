from __future__ import annotations

import os
import random
from pathlib import Path

from PIL import Image, ImageDraw

from CaptchaGenerator.core import CaptchaConfig, ChallengeResult, VisualChallenge
from CaptchaGenerator.exceptions import InvalidArgumentError


class SliderPuzzleCaptcha(VisualChallenge):
    def generate(self, *, image_path: str, name_export: str, path_export: str,
                 difficulty: str = "medium", tolerance: int = 8,
                 config: CaptchaConfig | None = None) -> ChallengeResult:
        if not os.path.exists(image_path):
            raise InvalidArgumentError(f"Image not found: {image_path}")
        size = {"easy": 84, "medium": 70, "hard": 58, "extreme": 48}.get(difficulty)
        if size is None:
            raise InvalidArgumentError("Unknown difficulty.")
        resolved = self._config(config)
        image = Image.open(image_path).convert("RGB").resize(resolved.size)
        x = random.randint(170, image.width - size - 30)
        y = random.randint(35, image.height - size - 35)
        piece = image.crop((x, y, x + size, y + size))
        background = image.copy()
        draw = ImageDraw.Draw(background, "RGBA")
        draw.rectangle((x, y, x + size, y + size), fill=(35, 42, 55, 190),
                       outline="white", width=3)
        piece_x = 25
        preview = background.copy()
        preview.paste(piece, (piece_x, y))
        ImageDraw.Draw(preview).rectangle(
            (piece_x, y, piece_x + size, y + size),
            outline=(20, 25, 35), width=3
        )
        output = Path(path_export)
        output.mkdir(parents=True, exist_ok=True)
        background_path = output / f"{name_export}_background.png"
        piece_path = output / f"{name_export}_piece.png"
        background.save(background_path)
        piece.save(piece_path)
        return self._save(preview, path_export=path_export, name_export=name_export,
                          answer=x,
                          prompt="Move the piece horizontally into the empty slot.",
                          metadata={"piece_start_x": piece_x, "target_x": x,
                                    "target_y": y, "piece_size": size,
                                    "tolerance": tolerance,
                                    "background_path": str(background_path),
                                    "piece_path": str(piece_path)},
                          config=resolved)
