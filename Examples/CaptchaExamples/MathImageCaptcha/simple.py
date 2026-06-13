from pathlib import Path
import sys

sys.path.insert(0, str(Path(__file__).parents[1]))
from _shared import FONTS, output_dir, show_result
from CaptchaGenerator import CaptchaConfig, MathImageCaptcha

result = MathImageCaptcha(CaptchaConfig(width=720, height=240)).generate(
    name_export="math_image", path_export=str(output_dir(__file__)),
    fonts=FONTS, difficulty="hard", style="wave",
)
show_result(result)
