from __future__ import annotations

import os
import random

from CaptchaGenerator.base import BaseCaptchaGenerator


class ImageDirectionCaptcha(BaseCaptchaGenerator):
    """Generator for captchas based on image file naming conventions for directions."""

    DIRECTION_KEYWORDS: dict[str, str] = {
        "Up": "Up",
        "Down": "Down",
        "Left": "Left",
        "Right": "Right",
        "UpRight": "UpRight",
        "DownRight": "DownRight",
        "DownLeft": "DownLeft",
        "UpLeft": "UpLeft",
    }
    # Backward compatibility with legacy direction icons/names
    _LEGACY_MAP: dict[str, str] = {
        "Bottom": "Down",
        "BottomRight": "DownRight",
        "BottomLeft": "DownLeft",
    }
    
    IMAGE_FORMATS: frozenset[str] = frozenset({".png", ".jpg", ".jpeg"})

    def generate(self, *, folder_path: str | None = None) -> tuple[str, str]:
        """Detect the direction of a random image based on its filename.

        Args:
            folder_path: Path to the directory containing direction-named images.
                If None, uses the directory of the current file.

        Returns:
            A tuple containing (image_filename, direction_key e.g. "UpRight").

        Raises:
            InvalidArgumentError: If no valid images are found.
        """
        search_path = folder_path if folder_path else os.path.dirname(os.path.abspath(__file__))

        image_list = [
            entry.name for entry in os.scandir(search_path)
            if entry.is_file() and os.path.splitext(entry.name)[1].lower() in self.IMAGE_FORMATS
        ]

        if not image_list:
            from CaptchaGenerator.exceptions import InvalidArgumentError
            raise InvalidArgumentError(f"No valid images found in {search_path}")

        random_image = random.choice(image_list)
        detected_direction = ""

        sorted_keywords = sorted(
            list(self.DIRECTION_KEYWORDS.keys()) + list(self._LEGACY_MAP.keys()),
            key=len,
            reverse=True
        )

        for keyword in sorted_keywords:
            if keyword in random_image:
                detected_direction = self.DIRECTION_KEYWORDS.get(keyword) or self._LEGACY_MAP.get(keyword, "")
                break

        return random_image, detected_direction
