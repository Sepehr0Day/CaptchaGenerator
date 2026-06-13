from pathlib import Path
import sys

sys.path.insert(0, str(Path(__file__).parents[1]))
from _shared import ASSETS
from CaptchaGenerator import ImageDirectionCaptcha

filename, direction = ImageDirectionCaptcha().generate(
    folder_path=str(ASSETS / "direction_images")
)
print("Image:", filename)
print("Direction:", direction)
