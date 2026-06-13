from pathlib import Path
import sys

from PIL import Image, ImageDraw

sys.path.insert(0, str(Path(__file__).parents[1]))
from _shared import FONTS, output_dir, show_result
from CaptchaGenerator import AnalogClockCaptcha, CaptchaConfig


def watermark(image: Image.Image, context: dict[str, object]) -> Image.Image:
    output = image.copy()
    draw = ImageDraw.Draw(output)
    draw.text((16, output.height - 28), "Custom App", fill="#334155")
    return output


config = CaptchaConfig(
    width=960,
    height=540,
    output_format="WEBP",
    quality=85,
    background_color="#f8fafc",
    foreground_color="#172033",
    accent_colors=("#ef4444", "#3b82f6", "#22c55e"),
    fonts=tuple(FONTS),
    font_size=42,
    line_width=4,
    padding=32,
    language="en",
    prompt="Read the custom clock",
    accessibility_text="An accessible analog clock captcha",
    high_contrast=True,
    include_answer_in_metadata=True,
    random_seed=50,
    post_render_hook=watermark,
)
result = AnalogClockCaptcha(config).generate(
    name_export="fully_customized", path_export=str(output_dir(__file__)),
)
show_result(result)
