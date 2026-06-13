from pathlib import Path
import sys

sys.path.insert(0, str(Path(__file__).parents[1]))
from _shared import FONTS, output_dir, show_result
from CaptchaGenerator import AnalogClockCaptcha, CaptchaConfig

config = CaptchaConfig(
    width=720, height=480, fonts=tuple(FONTS), line_width=4,
    accent_colors=("#d33f49", "#3478c8", "#2a9d6f"),
)
result = AnalogClockCaptcha(config).generate(
    name_export="clock", path_export=str(output_dir(__file__)),
    minute_step=5, show_numbers=True, twenty_four_hour_answer=False,
)
show_result(result)
