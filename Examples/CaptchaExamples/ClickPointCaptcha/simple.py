from pathlib import Path
import sys

sys.path.insert(0, str(Path(__file__).parents[1]))
from _shared import output_dir, show_result
from CaptchaGenerator import CaptchaConfig, ClickPointCaptcha

result = ClickPointCaptcha(
    CaptchaConfig(width=720, height=420, accessibility_text="Click the circle")
).generate(
    name_export="click_point", path_export=str(output_dir(__file__)),
    target="circle",
)
show_result(result)
print("Accept clicks within:", result.metadata["tolerance"], "pixels")
