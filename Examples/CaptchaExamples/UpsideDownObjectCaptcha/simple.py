from pathlib import Path
import sys

sys.path.insert(0, str(Path(__file__).parents[1]))
from _shared import output_dir, show_result
from CaptchaGenerator import CaptchaConfig, UpsideDownObjectCaptcha

result = UpsideDownObjectCaptcha(
    CaptchaConfig(width=800, height=480, random_seed=21)
).generate(
    name_export="upside_down", path_export=str(output_dir(__file__)),
    item_count=12, rotation=180,
)
show_result(result)
