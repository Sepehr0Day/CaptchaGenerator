from __future__ import annotations

import os
import random

from CaptchaGenerator.base import BaseCaptchaGenerator
from CaptchaGenerator.exceptions import CaptchaError


class AudioCaptcha(BaseCaptchaGenerator):
    """Generator for audio-based captchas using Google Text-to-Speech."""

    def generate(
        self,
        *,
        number_gen: int,
        values_captcha: str,
        name_export: str,
        path_export: str,
    ) -> tuple[str, str]:
        """Generate an audio captcha MP3 file.

        Args:
            number_gen: Number of characters to generate.
            values_captcha: String of possible characters.
            name_export: Filename for the exported MP3.
            path_export: Directory path for the exported MP3.

        Returns:
            A tuple containing (captcha_text, full_mp3_path).
        """
        try:
            from gtts import gTTS
        except ImportError as exc:
            raise CaptchaError(
                "AudioCaptcha requires the optional 'gTTS' package. "
                "Install audio support for the active Python interpreter with: "
                'python -m pip install "CaptchaGenerator[audio]"'
            ) from exc

        captcha_values = [random.choice(values_captcha) for _ in range(int(number_gen))]
        captcha_text = "".join(captcha_values)
        
        # Add commas between characters to slow down TTS for clarity
        tts_text = ",".join(list(captcha_text))
        
        tts = gTTS(text=tts_text, lang="en")
        
        if not os.path.exists(path_export):
            os.makedirs(path_export, exist_ok=True)
            
        full_path = os.path.join(path_export, f"{name_export}.mp3")
        tts.save(full_path)
        
        return captcha_text, full_path
