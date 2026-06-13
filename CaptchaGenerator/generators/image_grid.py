from __future__ import annotations

import random
from pathlib import Path

from PIL import Image, ImageDraw

from CaptchaGenerator.exceptions import InvalidArgumentError
from CaptchaGenerator.core import ChallengeResult, VisualChallenge


class ImageGridCaptcha(VisualChallenge):
    def generate(self, *, path_folder: str, target_name: str, name_export: str,
                 path_export: str, grid_size: int = 3) -> ChallengeResult:
        files = [path for path in Path(path_folder).iterdir()
                 if path.suffix.lower() in {".png", ".jpg", ".jpeg"}]
        targets = [path for path in files if target_name.lower() in path.stem.lower()]
        distractors = [path for path in files if path not in targets]
        cells = grid_size * grid_size
        if not targets or not distractors:
            raise InvalidArgumentError("Folder needs target and distractor images.")
        target_count = min(len(targets), random.randint(1, min(3, cells - 1)))
        chosen = random.sample(targets, target_count)
        chosen += [random.choice(distractors) for _ in range(cells - target_count)]
        random.shuffle(chosen)
        image, answers = Image.new("RGB", (720, 720), "white"), []
        cell, draw = 720 // grid_size, None
        draw = ImageDraw.Draw(image)
        for index, path in enumerate(chosen):
            tile = Image.open(path).convert("RGB")
            tile.thumbnail((cell - 12, cell - 12))
            column, row = index % grid_size, index // grid_size
            image.paste(tile, (column * cell + (cell - tile.width) // 2,
                               row * cell + (cell - tile.height) // 2))
            draw.rectangle((column * cell, row * cell, (column + 1) * cell - 1,
                            (row + 1) * cell - 1), outline=(60, 70, 85), width=3)
            if path in targets:
                answers.append(index)
        return self._save(image, path_export=path_export, name_export=name_export,
                          answer=answers,
                          prompt=f"Select every tile containing {target_name}.",
                          metadata={"grid_size": grid_size,
                                    "answer_is_zero_based": True})
