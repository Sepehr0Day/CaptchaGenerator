from pathlib import Path
import sys

sys.path.insert(0, str(Path(__file__).parents[1]))
from _shared import ASSETS, FONTS, output_dir
from CaptchaGenerator import CaptchaConfig, WordCaptcha

output = output_dir(__file__)
answer = WordCaptcha(CaptchaConfig(width=720, height=240)).generate(
    backgrounds=[], path_words=str(ASSETS / "words.txt"), fonts=FONTS,
    font_size=100, name_export="word", path_export=str(output),
    difficulty="medium", style="arc",
)
print("Answer:", answer)
