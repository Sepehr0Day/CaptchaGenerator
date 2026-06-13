from __future__ import annotations

import os
import random
from typing import Any

from PIL import Image

from CaptchaGenerator.base import BaseCaptchaGenerator
from CaptchaGenerator.core.config import CaptchaConfig
from CaptchaGenerator.core.result import ChallengeResult


class VisualChallenge(BaseCaptchaGenerator):
    """Base for configurable image challenges."""

    def __init__(self, config: CaptchaConfig | None = None) -> None:
        super().__init__(config or CaptchaConfig(height=420))

    def _config(self, config: CaptchaConfig | None) -> CaptchaConfig:
        resolved = config or self.config
        if resolved.random_seed is not None:
            random.seed(resolved.random_seed)
        return resolved

    def _prepare(
        self, image: Image.Image, config: CaptchaConfig, context: dict[str, Any]
    ) -> Image.Image:
        output = image
        if config.pre_render_hook:
            output = config.pre_render_hook(output, context)
        if output.size != config.size:
            output = output.resize(config.size, Image.Resampling.LANCZOS)
        if config.post_render_hook:
            output = config.post_render_hook(output, context)
        return output

    def _save(
        self,
        image: Image.Image,
        *,
        path_export: str,
        name_export: str,
        answer: Any,
        prompt: str,
        metadata: dict[str, Any] | None = None,
        config: CaptchaConfig | None = None,
    ) -> ChallengeResult:
        resolved = self._config(config)
        final_prompt = resolved.prompt or prompt
        final_metadata = dict(metadata or {})
        if resolved.include_answer_in_metadata:
            final_metadata["answer"] = answer
        context = {
            "answer": answer,
            "prompt": final_prompt,
            "metadata": final_metadata,
        }
        image = self._prepare(image, resolved, context)
        os.makedirs(path_export, exist_ok=True)
        extension = resolved.extension
        path = os.path.join(path_export, f"{name_export}.{extension}")
        save_kwargs: dict[str, Any] = {}
        if resolved.output_format.upper() in {"JPEG", "JPG", "WEBP"}:
            save_kwargs["quality"] = resolved.quality
        image.save(path, format=resolved.output_format, **save_kwargs)
        mime = f"image/{'jpeg' if extension == 'jpg' else extension}"
        accessibility = (
            resolved.accessibility_text
            or f"Captcha challenge. {final_prompt}"
        )
        return ChallengeResult(
            answer,
            path,
            final_prompt,
            final_metadata,
            accessibility,
            mime,
        )
