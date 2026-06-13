from pathlib import Path
import sys

sys.path.insert(0, str(Path(__file__).parents[1]))
from _shared import FONTS, output_dir, show_result
from CaptchaGenerator import CaptchaConfig, ShapeCountCaptcha

for difficulty in ("easy", "medium", "hard", "extreme"):
    result = ShapeCountCaptcha(CaptchaConfig(width=720, height=420)).generate(
        name_export=f"shape_count_{difficulty}",
        path_export=str(output_dir(__file__)), fonts=FONTS,
        difficulty=difficulty,
    )
    show_result(result)
