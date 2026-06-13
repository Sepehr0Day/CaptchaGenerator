from pathlib import Path
import sys

sys.path.insert(0, str(Path(__file__).parents[1]))
from _shared import output_dir, show_result
from CaptchaGenerator import CaptchaConfig, IrregularPuzzleCaptcha

result = IrregularPuzzleCaptcha(
    CaptchaConfig(width=800, height=480, random_seed=31)
).generate(
    name_export="irregular_puzzle", path_export=str(output_dir(__file__)),
    vertices=9, piece_radius=55, tolerance=10,
)
show_result(result)
