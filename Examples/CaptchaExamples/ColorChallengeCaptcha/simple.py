from pathlib import Path
import sys

sys.path.insert(0, str(Path(__file__).parents[1]))
from _shared import FONTS, output_dir, show_result
from CaptchaGenerator import CaptchaConfig, ColorChallengeCaptcha

result = ColorChallengeCaptcha(
    CaptchaConfig(width=720, height=300, high_contrast=True)
).generate(
    name_export="color_challenge", path_export=str(output_dir(__file__)),
    fonts=FONTS,
)
show_result(result)
