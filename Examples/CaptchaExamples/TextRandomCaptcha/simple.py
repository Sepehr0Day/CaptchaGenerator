from pathlib import Path
import sys

sys.path.insert(0, str(Path(__file__).parents[1]))
from _shared import FONTS, VALUES, output_dir
from CaptchaGenerator import CaptchaConfig, TextRandomCaptcha

output = output_dir(__file__)
generator = TextRandomCaptcha(CaptchaConfig(width=720, height=240, random_seed=11))
answer, variants = generator.generate(
    number_gen=6, values_captcha=VALUES, number_variants=5,
    backgrounds=[], fonts=FONTS, name_export="random_text",
    path_export=str(output), difficulty="hard", style="wave",
)
print("Answer:", answer)
print("Variants:", variants)
