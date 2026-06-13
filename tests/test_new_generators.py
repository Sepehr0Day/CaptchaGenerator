from __future__ import annotations

from pathlib import Path

from PIL import Image

from CaptchaGenerator import (
    AnalogClockCaptcha,
    CaptchaConfig,
    CustomQuestionCaptcha,
    IrregularPuzzleCaptcha,
    MazeCaptcha,
    PatternCompletionCaptcha,
    Perspective3DCaptcha,
    UpsideDownObjectCaptcha,
)


def assert_image(path: str, size: tuple[int, int]) -> None:
    with Image.open(path) as image:
        assert image.size == size


def test_new_generators(tmp_path: Path) -> None:
    config = CaptchaConfig(
        width=640,
        height=400,
        output_format="PNG",
        accessibility_text="Accessible captcha",
        random_seed=42,
    )
    results = [
        AnalogClockCaptcha(config).generate(
            name_export="clock", path_export=str(tmp_path)
        ),
        UpsideDownObjectCaptcha(config).generate(
            name_export="upside",
            path_export=str(tmp_path),
        ),
        Perspective3DCaptcha(config).generate(
            name_export="perspective", path_export=str(tmp_path)
        ),
        CustomQuestionCaptcha(config).generate(
            name_export="custom",
            path_export=str(tmp_path),
            question="What is two plus two?",
            answer=4,
        ),
        IrregularPuzzleCaptcha(config).generate(
            name_export="irregular",
            path_export=str(tmp_path),
        ),
        PatternCompletionCaptcha(config).generate(
            name_export="pattern", path_export=str(tmp_path)
        ),
        MazeCaptcha(config).generate(
            name_export="maze", path_export=str(tmp_path)
        ),
    ]
    for result in results:
        assert result.answer is not None
        assert result.accessibility_text == "Accessible captcha"
        assert_image(result.path, config.size)


def test_custom_output_format_and_hooks(tmp_path: Path) -> None:
    calls = []

    def hook(image: Image.Image, context: dict[str, object]) -> Image.Image:
        calls.append(context)
        return image

    config = CaptchaConfig(
        width=500,
        height=320,
        output_format="WEBP",
        quality=80,
        prompt="Custom prompt",
        include_answer_in_metadata=True,
        post_render_hook=hook,
    )
    result = AnalogClockCaptcha(config).generate(
        name_export="custom_clock", path_export=str(tmp_path)
    )
    assert result.path.endswith(".webp")
    assert result.prompt == "Custom prompt"
    assert "answer" in result.metadata
    assert calls
