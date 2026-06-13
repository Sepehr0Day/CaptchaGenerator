from pathlib import Path
import sys

sys.path.insert(0, str(Path(__file__).parents[1]))
from _shared import output_dir, show_result
from CaptchaGenerator import CaptchaConfig, PatternCompletionCaptcha

result = PatternCompletionCaptcha(
    CaptchaConfig(width=900, height=480, random_seed=32)
).generate(
    name_export="pattern", path_export=str(output_dir(__file__)),
    pattern_length=8, option_count=4,
)
show_result(result)
