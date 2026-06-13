from __future__ import annotations

import os
import random

from CaptchaGenerator.base import BaseCaptchaGenerator


class ImageRandomCaptcha(BaseCaptchaGenerator):
    """Generator for selecting random images from a folder as captchas."""

    SUPPORTED_FORMATS: frozenset[str] = frozenset({".jpg", ".jpeg", ".png"})

    def generate(
        self,
        *,
        path_folder: str,
        number_random_select: int,
    ) -> tuple[str, str, str, list[str]]:
        """Select random images from a folder and return details.

        Args:
            path_folder: Path to the directory containing images.
            number_random_select: Number of random images to return names for.

        Returns:
            A tuple containing:
            (selected_filename, selected_name, selected_extension, all_selected_names)
        
        Raises:
            InvalidArgumentError: If the folder is empty or no valid images found.
        """
        if not os.path.exists(path_folder):
            from CaptchaGenerator.exceptions import InvalidArgumentError
            raise InvalidArgumentError(f"Folder not found: {path_folder}")

        image_list = [
            f for f in os.listdir(path_folder)
            if os.path.isfile(os.path.join(path_folder, f))
            and os.path.splitext(f)[1].lower() in self.SUPPORTED_FORMATS
        ]

        if not image_list:
            from CaptchaGenerator.exceptions import InvalidArgumentError
            raise InvalidArgumentError(f"No valid images found in {path_folder}")

        # Ensure we don't try to select more than available
        count = min(int(number_random_select), len(image_list))
        random_image_list = random.sample(image_list, count)
        
        selected_file = random.choice(random_image_list)
        name, ext = os.path.splitext(selected_file)
        
        all_names = [os.path.splitext(img)[0] for img in random_image_list]

        return selected_file, name, ext, all_names
