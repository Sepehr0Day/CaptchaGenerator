from pathlib import Path
import sys

sys.path.insert(0, str(Path(__file__).parents[1]))
from _shared import ASSETS
from CaptchaGenerator import ImageRandomCaptcha

result = ImageRandomCaptcha().generate(
    path_folder=str(ASSETS / "random_images"), number_random_select=3
)
print(result)
