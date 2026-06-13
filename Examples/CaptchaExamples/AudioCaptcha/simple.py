from pathlib import Path
import sys

sys.path.insert(0, str(Path(__file__).parents[1]))
from _shared import VALUES, output_dir
from CaptchaGenerator import AudioCaptcha

# gTTS requires an internet connection.
answer, path = AudioCaptcha().generate(
    number_gen=6, values_captcha=VALUES, name_export="audio",
    path_export=str(output_dir(__file__)),
)
print("Answer:", answer)
print("Output:", path)
