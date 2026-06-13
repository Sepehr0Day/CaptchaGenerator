from pathlib import Path
import sys

sys.path.insert(0, str(Path(__file__).parents[1]))
from _shared import FONTS, output_dir, show_result
from CaptchaGenerator import CaptchaConfig, Perspective3DCaptcha

result = Perspective3DCaptcha(
    CaptchaConfig(width=720, height=480, fonts=tuple(FONTS))
).generate(
    name_export="perspective_3d", path_export=str(output_dir(__file__)),
    labels=("1", "2", "3"), ask_face="right", skew=0.42,
)
show_result(result)
