from pathlib import Path
import sys

sys.path.insert(0, str(Path(__file__).parents[1]))
from _shared import ASSETS, output_dir, show_result
from CaptchaGenerator import CaptchaConfig, RotateImageCaptcha

result = RotateImageCaptcha(CaptchaConfig(width=720, height=420)).generate(
    image_path=str(ASSETS / "direction_images" / "test_Up.png"),
    name_export="rotate", path_export=str(output_dir(__file__)),
)
show_result(result)
