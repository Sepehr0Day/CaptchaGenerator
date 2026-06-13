from __future__ import annotations

import ast
import operator
from pathlib import Path

import pytest
from PIL import Image

from CaptchaGenerator import (
    Captcha,
    DIFFICULTIES,
    STYLES,
    ImageDirectionCaptcha,
    ImageRandomCaptcha,
    MathCaptcha,
    TextCaptcha,
    TextRandomCaptcha,
    WordCaptcha,
)
from CaptchaGenerator.exceptions import InvalidArgumentError

VALUES = "ABCDEFGHJKLMNPQRSTUVWXYZ23456789"


@pytest.fixture
def font() -> list[str]:
    path = Path(r"C:\Windows\Fonts\arial.ttf")
    return [str(path)] if path.exists() else []


def assert_valid_image(path: Path) -> None:
    with Image.open(path) as image:
        assert image.size == (720, 240)
        assert image.mode == "RGB"
        assert image.getbbox() is not None


def test_text_captcha_generates_image(tmp_path: Path, font: list[str]) -> None:
    answer = TextCaptcha().generate(
        number_gen=6,
        values_captcha=VALUES,
        name_export="text",
        path_export=str(tmp_path),
        fonts=font,
        colors=["navy", "darkred"],
        backgrounds=[],
    )
    assert len(answer) == 6
    assert set(answer) <= set(VALUES)
    assert_valid_image(tmp_path / "text.png")


def test_text_captcha_allows_repeated_pool(
    tmp_path: Path, font: list[str]
) -> None:
    answer = TextCaptcha().generate(
        number_gen=8,
        values_captcha="A",
        name_export="repeat",
        path_export=str(tmp_path),
        fonts=font,
        colors=["black"],
        backgrounds=[],
    )
    assert answer == "A" * 8


def test_random_text_captcha(tmp_path: Path, font: list[str]) -> None:
    answer, variants = TextRandomCaptcha().generate(
        number_gen=6,
        values_captcha=VALUES,
        number_variants=5,
        backgrounds=[],
        fonts=font,
        name_export="random",
        path_export=str(tmp_path),
    )
    assert len(variants) == 5
    assert answer in variants
    assert_valid_image(tmp_path / "random.png")


def test_word_captcha(tmp_path: Path, font: list[str]) -> None:
    words = tmp_path / "words.txt"
    words.write_text("Alpha\nBravo\n", encoding="utf-8")
    answer = WordCaptcha().generate(
        backgrounds=[],
        path_words=str(words),
        fonts=font,
        font_size=100,
        name_export="word",
        path_export=str(tmp_path),
    )
    assert answer in {"Alpha", "Bravo"}
    assert_valid_image(tmp_path / "word.png")


@pytest.mark.parametrize(
    ("length", "values", "colors"),
    [(0, VALUES, ["black"]), (3, "", ["black"]), (3, VALUES, [])],
)
def test_text_rejects_invalid_input(
    tmp_path: Path,
    font: list[str],
    length: int,
    values: str,
    colors: list[str],
) -> None:
    with pytest.raises(InvalidArgumentError):
        TextCaptcha().generate(
            number_gen=length,
            values_captcha=values,
            name_export="invalid",
            path_export=str(tmp_path),
            fonts=font,
            colors=colors,
            backgrounds=[],
        )


def test_random_text_rejects_zero_variants(
    tmp_path: Path, font: list[str]
) -> None:
    with pytest.raises(InvalidArgumentError):
        TextRandomCaptcha().generate(
            number_gen=5,
            values_captcha=VALUES,
            number_variants=0,
            backgrounds=[],
            fonts=font,
            name_export="invalid",
            path_export=str(tmp_path),
        )


def test_math_captcha_is_correct() -> None:
    operations = {ast.Add: operator.add, ast.Sub: operator.sub, ast.Mult: operator.mul}
    for _ in range(250):
        expression, result = MathCaptcha().generate()
        tree = ast.parse(expression, mode="eval").body
        assert isinstance(tree, ast.BinOp)
        assert operations[type(tree.op)](tree.left.value, tree.right.value) == result


def test_image_generators() -> None:
    assets = Path(__file__).parents[1] / "Examples" / "assets"
    selected, name, extension, names = ImageRandomCaptcha().generate(
        path_folder=str(assets / "random_images"),
        number_random_select=3,
    )
    assert selected == f"{name}{extension}"
    assert name in names

    filename, direction = ImageDirectionCaptcha().generate(
        folder_path=str(assets / "direction_images")
    )
    assert direction
    assert direction in filename


@pytest.mark.parametrize("difficulty", DIFFICULTIES)
@pytest.mark.parametrize("style", STYLES)
def test_all_difficulty_and_style_combinations(
    tmp_path: Path,
    font: list[str],
    difficulty: str,
    style: str,
) -> None:
    name = f"{style}_{difficulty}"
    TextCaptcha().generate(
        number_gen=6,
        values_captcha=VALUES,
        name_export=name,
        path_export=str(tmp_path),
        fonts=font,
        colors=["navy", "darkred"],
        backgrounds=[],
        difficulty=difficulty,
        style=style,
    )
    assert_valid_image(tmp_path / f"{name}.png")


@pytest.mark.parametrize(
    ("difficulty", "style"),
    [("impossible", "modern"), ("medium", "unknown")],
)
def test_invalid_render_options_are_rejected(
    tmp_path: Path,
    font: list[str],
    difficulty: str,
    style: str,
) -> None:
    with pytest.raises(InvalidArgumentError):
        TextCaptcha().generate(
            number_gen=6,
            values_captcha=VALUES,
            name_export="invalid_options",
            path_export=str(tmp_path),
            fonts=font,
            colors=["navy"],
            backgrounds=[],
            difficulty=difficulty,
            style=style,
        )


def test_legacy_api_accepts_render_options(
    tmp_path: Path, font: list[str]
) -> None:
    answer = Captcha.CaptchaGenerat(
        NumberGen=6,
        ValuesCaptcha=VALUES,
        NameExport="legacy",
        PathExport=str(tmp_path),
        Fonts=font,
        Colors=["navy"],
        Backgrounds=[],
        Difficulty="hard",
        Style="mesh",
    )
    assert len(answer) == 6
    assert_valid_image(tmp_path / "legacy.png")
