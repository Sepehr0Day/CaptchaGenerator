from pathlib import Path
import sys

sys.path.insert(0, str(Path(__file__).parents[1]))
from _shared import FONTS, output_dir, show_result
from CaptchaGenerator import CaptchaConfig, LogicChallengeCaptcha

result = LogicChallengeCaptcha(CaptchaConfig(width=900, height=300)).generate(
    name_export="logic", path_export=str(output_dir(__file__)),
    fonts=FONTS, difficulty="medium",
)
show_result(result)
