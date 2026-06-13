from pathlib import Path
import sys

sys.path.insert(0, str(Path(__file__).parents[1]))
from _shared import FONTS, output_dir, show_result
from CaptchaGenerator import CaptchaConfig, CustomQuestionCaptcha

questions = [
    ("What is the capital of France?", "Paris"),
    ("How many days are in a week?", 7),
    ("Type the word shown in this instruction: BLUE", "BLUE"),
]
result = CustomQuestionCaptcha(
    CaptchaConfig(width=900, height=360, fonts=tuple(FONTS), font_size=44)
).generate(
    name_export="custom_question", path_export=str(output_dir(__file__)),
    questions=questions,
)
show_result(result)
