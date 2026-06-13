from __future__ import annotations

from CaptchaGenerator.exceptions import CaptchaError, InvalidArgumentError
from CaptchaGenerator.core import CaptchaConfig, DIFFICULTIES, STYLES
from CaptchaGenerator.generators import (
    AnalogClockCaptcha,
    AnimatedCaptcha,
    AudioCaptcha,
    ChallengeResult,
    ClickPointCaptcha,
    ColorChallengeCaptcha,
    CustomQuestionCaptcha,
    ImageGridCaptcha,
    ImageDirectionCaptcha,
    ImageRandomCaptcha,
    LogicChallengeCaptcha,
    IrregularPuzzleCaptcha,
    MazeCaptcha,
    MathImageCaptcha,
    MathCaptcha,
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
    SUPPORTED_CAPTCHAS,
)

__version__ = "2.0.0"


class Captcha:
    """Legacy compatibility shim. Use the individual generator classes instead."""

    @staticmethod
    def CaptchaGenerat(
        NumberGen: int | None = None,
        ValuesCaptcha: str | None = None,
        NameExport: str | None = None,
        PathExport: str | None = None,
        Fonts: list[str] | None = None,
        Colors: list[str] | None = None,
        Backgrounds: list[str] | None = None,
        Difficulty: str = "medium",
        Style: str = "modern",
    ) -> str:
        """Legacy wrapper for TextCaptcha."""
        if any(v is None for v in (NumberGen, ValuesCaptcha, NameExport, PathExport, Fonts, Colors, Backgrounds)):
            raise InvalidArgumentError("All arguments are required.")
        
        return TextCaptcha().generate(
            number_gen=NumberGen,  # type: ignore
            values_captcha=ValuesCaptcha,  # type: ignore
            name_export=NameExport,  # type: ignore
            path_export=PathExport,  # type: ignore
            fonts=Fonts,  # type: ignore
            colors=Colors,  # type: ignore
            backgrounds=Backgrounds,  # type: ignore
            difficulty=Difficulty,
            style=Style,
        )

    @staticmethod
    def CaptchaGeneratRandom(
        NumberGen: int | None = None,
        ValuesCaptcha: str | None = None,
        NumberVariants: int | None = None,
        Backgrounds: list[str] | None = None,
        Fonts: list[str] | None = None,
        NameExport: str | None = None,
        PathExport: str | None = None,
        Difficulty: str = "medium",
        Style: str = "modern",
    ) -> tuple[str, list[str]]:
        """Legacy wrapper for TextRandomCaptcha."""
        if any(v is None for v in (NumberGen, ValuesCaptcha, NumberVariants, Backgrounds, Fonts, NameExport, PathExport)):
            raise InvalidArgumentError("All arguments are required.")

        return TextRandomCaptcha().generate(
            number_gen=NumberGen,  # type: ignore
            values_captcha=ValuesCaptcha,  # type: ignore
            number_variants=NumberVariants,  # type: ignore
            backgrounds=Backgrounds,  # type: ignore
            fonts=Fonts,  # type: ignore
            name_export=NameExport,  # type: ignore
            path_export=PathExport,  # type: ignore
            difficulty=Difficulty,
            style=Style,
        )

    @staticmethod
    def CaptchaGeneratorImageRandom(
        PathFolder: str, NumberRandomSelect: int
    ) -> tuple[str, str, str, list[str]]:
        """Legacy wrapper for ImageRandomCaptcha."""
        return ImageRandomCaptcha().generate(
            path_folder=PathFolder, number_random_select=NumberRandomSelect
        )

    @staticmethod
    def CaptchaGeneratorIDR(FolderImagesAddress: str | None = None) -> tuple[str, str]:
        """Legacy wrapper for ImageDirectionCaptcha."""
        return ImageDirectionCaptcha().generate(folder_path=FolderImagesAddress)

    @staticmethod
    def CaptchaGeneratorAudio(
        NumberGen: int | None = None,
        ValuesCaptcha: str | None = None,
        NameExport: str | None = None,
        PathExport: str | None = None,
    ) -> tuple[str, str]:
        """Legacy wrapper for AudioCaptcha."""
        if any(v is None for v in (NumberGen, ValuesCaptcha, NameExport, PathExport)):
            raise InvalidArgumentError("All arguments are required.")
            
        return AudioCaptcha().generate(
            number_gen=NumberGen,  # type: ignore
            values_captcha=ValuesCaptcha,  # type: ignore
            name_export=NameExport,  # type: ignore
            path_export=PathExport,  # type: ignore
        )

    @staticmethod
    def CaptchaGeneratorMath() -> tuple[str, int]:
        """Legacy wrapper for MathCaptcha."""
        return MathCaptcha().generate()

    @staticmethod
    def CaptchaGeneratRandomWord(
        Backgrounds: list[str] | None = None,
        PathWords: str | None = None,
        Fonts: list[str] | None = None,
        FontSize: int | None = None,
        NameExport: str | None = None,
        PathExport: str | None = None,
        Difficulty: str = "medium",
        Style: str = "modern",
    ) -> str:
        """Legacy wrapper for WordCaptcha."""
        if any(v is None for v in (Backgrounds, PathWords, Fonts, FontSize, NameExport, PathExport)):
            raise InvalidArgumentError("All arguments are required.")

        return WordCaptcha().generate(
            backgrounds=Backgrounds,  # type: ignore
            path_words=PathWords,  # type: ignore
            fonts=Fonts,  # type: ignore
            font_size=FontSize,  # type: ignore
            name_export=NameExport,  # type: ignore
            path_export=PathExport,  # type: ignore
            difficulty=Difficulty,
            style=Style,
        )


__all__ = [
    "Captcha",
    "CaptchaConfig",
    "TextCaptcha",
    "TextRandomCaptcha",
    "WordCaptcha",
    "MathCaptcha",
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
    "UpsideDownObjectCaptcha",
    "ImageRandomCaptcha",
    "ImageDirectionCaptcha",
    "CaptchaError",
    "InvalidArgumentError",
    "DIFFICULTIES",
    "STYLES",
    "SUPPORTED_CAPTCHAS",
]
