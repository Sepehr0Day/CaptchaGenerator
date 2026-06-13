from pathlib import Path
import sys

sys.path.insert(0, str(Path(__file__).parents[1]))
from _shared import output_dir, show_result
from CaptchaGenerator import CaptchaConfig, OddOneOutCaptcha

result = OddOneOutCaptcha(CaptchaConfig(width=720, height=420)).generate(
    name_export="odd_one_out", path_export=str(output_dir(__file__)),
    difficulty="hard",
)
show_result(result)
