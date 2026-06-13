from pathlib import Path
import sys

sys.path.insert(0, str(Path(__file__).parents[1]))
from _shared import FONTS, output_dir, show_result
from CaptchaGenerator import CaptchaConfig, SequenceCaptcha

result = SequenceCaptcha(CaptchaConfig(width=900, height=260)).generate(
    name_export="sequence", path_export=str(output_dir(__file__)),
    fonts=FONTS, difficulty="hard", style="minimal",
)
show_result(result)
