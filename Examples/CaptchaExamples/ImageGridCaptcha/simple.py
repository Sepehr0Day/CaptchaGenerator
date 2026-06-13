from pathlib import Path
import sys

sys.path.insert(0, str(Path(__file__).parents[1]))
from _shared import ASSETS, output_dir, show_result
from CaptchaGenerator import CaptchaConfig, ImageGridCaptcha

result = ImageGridCaptcha(CaptchaConfig(width=720, height=720)).generate(
    path_folder=str(ASSETS / "random_images"), target_name="Tree",
    name_export="image_grid", path_export=str(output_dir(__file__)),
    grid_size=3,
)
show_result(result)
