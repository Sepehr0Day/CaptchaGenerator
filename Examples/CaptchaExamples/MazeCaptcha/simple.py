from pathlib import Path
import sys

sys.path.insert(0, str(Path(__file__).parents[1]))
from _shared import output_dir, show_result
from CaptchaGenerator import CaptchaConfig, MazeCaptcha

output = output_dir(__file__)
for answer_mode in ("directions", "path", "exit"):
    result = MazeCaptcha(
        CaptchaConfig(width=900, height=600, random_seed=40)
    ).generate(
        name_export=f"maze_{answer_mode}", path_export=str(output),
        columns=14, rows=9, answer_mode=answer_mode,
    )
    show_result(result)
