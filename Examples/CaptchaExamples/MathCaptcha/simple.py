from pathlib import Path
import sys

sys.path.insert(0, str(Path(__file__).parents[1]))
import _shared  # noqa: F401

from CaptchaGenerator import MathCaptcha

for _ in range(5):
    expression, answer = MathCaptcha().generate()
    print(expression, "=", answer)
