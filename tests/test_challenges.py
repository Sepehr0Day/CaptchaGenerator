from __future__ import annotations

from pathlib import Path

from PIL import Image

from CaptchaGenerator import (
    AnimatedCaptcha,
    ChallengeResult,
    ClickPointCaptcha,
    ColorChallengeCaptcha,
    ImageGridCaptcha,
    IrregularPuzzleCaptcha,
    LogicChallengeCaptcha,
    MathImageCaptcha,
    MissingCharacterCaptcha,
    OddOneOutCaptcha,
    RotateImageCaptcha,
    SequenceCaptcha,
    ShapeCountCaptcha,
    SliderPuzzleCaptcha,
)


def font() -> list[str]:
    path = Path(r"C:\Windows\Fonts\arial.ttf")
    return [str(path)] if path.exists() else []


def assert_result(result: ChallengeResult, suffix: str = ".png") -> None:
    assert result.prompt
    assert Path(result.path).exists()
    assert Path(result.path).suffix == suffix
    with Image.open(result.path) as image:
        assert image.width > 100
        assert image.height > 100


def test_text_and_logic_challenges(tmp_path: Path) -> None:
    results = [
        MathImageCaptcha().generate(
            name_export="math_image",
            path_export=str(tmp_path),
            fonts=font(),
            difficulty="hard",
        ),
        MissingCharacterCaptcha().generate(
            name_export="missing",
            path_export=str(tmp_path),
            fonts=font(),
        ),
        SequenceCaptcha().generate(
            name_export="sequence",
            path_export=str(tmp_path),
            fonts=font(),
            difficulty="hard",
        ),
        ColorChallengeCaptcha().generate(
            name_export="color",
            path_export=str(tmp_path),
            fonts=font(),
        ),
        LogicChallengeCaptcha().generate(
            name_export="logic",
            path_export=str(tmp_path),
            fonts=font(),
        ),
    ]
    for result in results:
        assert_result(result)
        assert result.answer is not None


def test_sequence_has_a_valid_predictable_rule(tmp_path: Path) -> None:
    result = SequenceCaptcha().generate(
        name_export="predictable_sequence",
        path_export=str(tmp_path),
        fonts=font(),
        difficulty="hard",
    )
    sequence = result.metadata["sequence"]
    value = result.metadata["rule_value"]
    if result.metadata["rule"] == "arithmetic":
        assert all(
            right - left == value
            for left, right in zip(sequence, sequence[1:])
        )
        assert result.answer == sequence[-1] + value
    else:
        assert all(
            right == left * value
            for left, right in zip(sequence, sequence[1:])
        )
        assert result.answer == sequence[-1] * value


def test_shape_and_selection_challenges(tmp_path: Path) -> None:
    shape = ShapeCountCaptcha().generate(
        name_export="shape",
        path_export=str(tmp_path),
        fonts=font(),
        difficulty="hard",
    )
    odd = OddOneOutCaptcha().generate(
        name_export="odd",
        path_export=str(tmp_path),
        difficulty="hard",
    )
    click = ClickPointCaptcha().generate(
        name_export="click",
        path_export=str(tmp_path),
    )
    for result in (shape, odd, click):
        assert_result(result)
    assert isinstance(shape.answer, int) and shape.answer >= 2
    assert isinstance(odd.answer, int)
    assert isinstance(click.answer, tuple) and len(click.answer) == 2
    assert click.metadata["tolerance"] > 0


def test_image_based_challenges(tmp_path: Path) -> None:
    assets = Path(__file__).parents[1] / "Examples" / "assets"
    source = assets / "random_images" / "Tree.png"
    rotate = RotateImageCaptcha().generate(
        image_path=str(source),
        name_export="rotate",
        path_export=str(tmp_path),
    )
    slider = SliderPuzzleCaptcha().generate(
        image_path=str(source),
        name_export="slider",
        path_export=str(tmp_path),
        difficulty="hard",
    )
    grid = ImageGridCaptcha().generate(
        path_folder=str(assets / "random_images"),
        target_name="Tree",
        name_export="grid",
        path_export=str(tmp_path),
    )
    for result in (rotate, slider, grid):
        assert_result(result)
    assert rotate.answer in {"clockwise", "counterclockwise", "180"}
    assert slider.answer == slider.metadata["target_x"]
    assert grid.answer


def test_animated_captcha(tmp_path: Path) -> None:
    result = AnimatedCaptcha().generate(
        name_export="animated",
        path_export=str(tmp_path),
        fonts=font(),
        frame_count=3,
    )
    assert_result(result, ".gif")
    assert len(result.answer) == 6
    with Image.open(result.path) as image:
        assert image.n_frames == 3


def test_missing_character_uses_inferable_word(tmp_path: Path) -> None:
    result = MissingCharacterCaptcha().generate(
        name_export="missing_word",
        path_export=str(tmp_path),
        fonts=font(),
        word="APPLE",
        difficulty="easy",
        style="minimal",
    )
    assert result.metadata["source"] == "word"
    assert result.metadata["puzzle"].count("?") == 1
    assert result.answer in "APPLE"


def test_puzzle_generators_export_interactive_assets(tmp_path: Path) -> None:
    assets = Path(__file__).parents[1] / "Examples" / "assets"
    slider = SliderPuzzleCaptcha().generate(
        image_path=str(assets / "random_images" / "Apple.png"),
        name_export="slider_assets",
        path_export=str(tmp_path),
    )
    irregular = IrregularPuzzleCaptcha().generate(
        name_export="irregular_assets",
        path_export=str(tmp_path),
    )
    for result in (slider, irregular):
        assert Path(result.metadata["background_path"]).exists()
        assert Path(result.metadata["piece_path"]).exists()
        assert result.metadata["tolerance"] > 0
