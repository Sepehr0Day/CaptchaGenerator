from __future__ import annotations

from CaptchaGenerator.generators.audio import AudioCaptcha
from CaptchaGenerator.core import ChallengeResult
from CaptchaGenerator.generators.analog_clock import AnalogClockCaptcha
from CaptchaGenerator.generators.animated import AnimatedCaptcha
from CaptchaGenerator.generators.click_point import ClickPointCaptcha
from CaptchaGenerator.generators.color_challenge import ColorChallengeCaptcha
from CaptchaGenerator.generators.image_grid import ImageGridCaptcha
from CaptchaGenerator.generators.logic import LogicChallengeCaptcha
from CaptchaGenerator.generators.custom_question import CustomQuestionCaptcha
from CaptchaGenerator.generators.irregular_puzzle import IrregularPuzzleCaptcha
from CaptchaGenerator.generators.maze import MazeCaptcha
from CaptchaGenerator.generators.math_image import MathImageCaptcha
from CaptchaGenerator.generators.missing_character import MissingCharacterCaptcha
from CaptchaGenerator.generators.odd_one_out import OddOneOutCaptcha
from CaptchaGenerator.generators.pattern_completion import PatternCompletionCaptcha
from CaptchaGenerator.generators.perspective_3d import Perspective3DCaptcha
from CaptchaGenerator.generators.rotate_image import RotateImageCaptcha
from CaptchaGenerator.generators.sequence import SequenceCaptcha
from CaptchaGenerator.generators.shape_count import ShapeCountCaptcha
from CaptchaGenerator.generators.slider_puzzle import SliderPuzzleCaptcha
from CaptchaGenerator.generators.image_direction import ImageDirectionCaptcha
from CaptchaGenerator.generators.image_random import ImageRandomCaptcha
from CaptchaGenerator.generators.math_captcha import MathCaptcha
from CaptchaGenerator.generators.text import TextCaptcha
from CaptchaGenerator.generators.text_random import TextRandomCaptcha
from CaptchaGenerator.generators.upside_down import UpsideDownObjectCaptcha
from CaptchaGenerator.generators.word import WordCaptcha

SUPPORTED_CAPTCHAS = {
    cls.__name__: cls
    for cls in (
        AnalogClockCaptcha,
        AnimatedCaptcha,
        AudioCaptcha,
        ClickPointCaptcha,
        ColorChallengeCaptcha,
        CustomQuestionCaptcha,
        ImageDirectionCaptcha,
        ImageGridCaptcha,
        ImageRandomCaptcha,
        IrregularPuzzleCaptcha,
        LogicChallengeCaptcha,
        MathCaptcha,
        MathImageCaptcha,
        MazeCaptcha,
        MissingCharacterCaptcha,
        OddOneOutCaptcha,
        PatternCompletionCaptcha,
        Perspective3DCaptcha,
        RotateImageCaptcha,
        SequenceCaptcha,
        ShapeCountCaptcha,
        SliderPuzzleCaptcha,
        TextCaptcha,
        TextRandomCaptcha,
        UpsideDownObjectCaptcha,
        WordCaptcha,
    )
}

__all__ = [
    "AudioCaptcha",
    "AnalogClockCaptcha",
    "AnimatedCaptcha",
    "ChallengeResult",
    "ClickPointCaptcha",
    "ColorChallengeCaptcha",
    "CustomQuestionCaptcha",
    "ImageGridCaptcha",
    "LogicChallengeCaptcha",
    "IrregularPuzzleCaptcha",
    "MazeCaptcha",
    "MathImageCaptcha",
    "MissingCharacterCaptcha",
    "OddOneOutCaptcha",
    "PatternCompletionCaptcha",
    "Perspective3DCaptcha",
    "RotateImageCaptcha",
    "SequenceCaptcha",
    "ShapeCountCaptcha",
    "SliderPuzzleCaptcha",
    "ImageDirectionCaptcha",
    "ImageRandomCaptcha",
    "MathCaptcha",
    "TextCaptcha",
    "TextRandomCaptcha",
    "UpsideDownObjectCaptcha",
    "WordCaptcha",
    "SUPPORTED_CAPTCHAS",
]
