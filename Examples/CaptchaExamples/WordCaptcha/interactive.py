from pathlib import Path
import sys
import tkinter as tk

from PIL import Image, ImageTk

sys.path.insert(0, str(Path(__file__).parents[1]))
from _shared import ASSETS, FONTS, output_dir
from CaptchaGenerator import CaptchaConfig, WordCaptcha

output = output_dir(__file__)
expected = WordCaptcha(CaptchaConfig(width=720, height=240, random_seed=520)).generate(
    backgrounds=[],
    path_words=str(ASSETS / "words.txt"),
    fonts=FONTS,
    font_size=100,
    name_export="interactive_word",
    path_export=str(output),
    difficulty="medium",
    style="arc",
)
root = tk.Tk()
root.title("WordCaptcha")
photo = ImageTk.PhotoImage(Image.open(output / "interactive_word.png"))
tk.Label(root, image=photo).pack(padx=12, pady=12)
tk.Label(root, text="Type the word shown.", font=("Segoe UI", 12, "bold")).pack()
answer = tk.StringVar()
tk.Entry(root, textvariable=answer, font=("Segoe UI", 14), width=24).pack(pady=8)
status = tk.StringVar()
tk.Button(
    root, text="Verify",
    command=lambda: status.set(
        "Solved!" if answer.get().strip().casefold() == expected.casefold() else "Try again."
    ),
).pack()
tk.Label(root, textvariable=status).pack(pady=10)
root.mainloop()
