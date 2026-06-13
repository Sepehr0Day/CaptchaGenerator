from pathlib import Path
import sys

sys.path.insert(0, str(Path(__file__).parents[1]))
from _shared import FONTS, VALUES, output_dir, show_result
from CaptchaGenerator import AnimatedCaptcha, CaptchaConfig

result = AnimatedCaptcha(CaptchaConfig(width=720, height=240)).generate(
    name_export="animated", path_export=str(output_dir(__file__)),
    fonts=FONTS, values=VALUES, length=6, difficulty="hard",
    style="modern", frame_count=8,
)
show_result(result)
