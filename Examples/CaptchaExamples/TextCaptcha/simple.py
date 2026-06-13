from pathlib import Path
import sys

sys.path.insert(0, str(Path(__file__).parents[1]))
from _shared import FONTS, VALUES, output_dir
from CaptchaGenerator import CaptchaConfig, TextCaptcha

output = output_dir(__file__)
config = CaptchaConfig(width=720, height=240, output_format="PNG", random_seed=10)

for difficulty in ("easy", "medium", "hard", "extreme"):
    for style in ("modern", "minimal", "wave", "arc", "mesh"):
        answer = TextCaptcha(config).generate(
            number_gen=6, values_captcha=VALUES,
            name_export=f"{style}_{difficulty}", path_export=str(output),
            fonts=FONTS, colors=["navy", "darkred", "darkgreen"],
            backgrounds=[], difficulty=difficulty, style=style,
        )
        print(style, difficulty, answer)
