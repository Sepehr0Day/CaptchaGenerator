from __future__ import annotations

import sys
from pathlib import Path

ROOT = Path(__file__).parents[2]
if str(ROOT) not in sys.path:
    sys.path.insert(0, str(ROOT))

EXAMPLES = Path(__file__).parent
ASSETS = ROOT / "Examples" / "assets"
FONT = Path(r"C:\Windows\Fonts\arial.ttf")
FONTS = [str(FONT)] if FONT.exists() else []
VALUES = "ABCDEFGHJKLMNPQRSTUVWXYZ23456789"


def output_dir(script_file: str) -> Path:
    path = Path(script_file).parent / "output"
    path.mkdir(exist_ok=True)
    return path


def show_result(result: object) -> None:
    if hasattr(result, "path"):
        print(f"Prompt: {result.prompt}")
        print(f"Answer: {result.answer}")
        print(f"Output: {result.path}")
        print(f"Metadata: {result.metadata}")
    else:
        print(result)
