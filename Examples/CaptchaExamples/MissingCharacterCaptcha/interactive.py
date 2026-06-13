from pathlib import Path
import sys
import tkinter as tk

from PIL import Image, ImageTk

sys.path.insert(0, str(Path(__file__).parents[1]))
from _shared import FONTS, output_dir
from CaptchaGenerator import CaptchaConfig, MissingCharacterCaptcha

result = MissingCharacterCaptcha(CaptchaConfig(width=720, height=240)).generate(
    name_export="interactive_missing",
    path_export=str(output_dir(__file__)),
    fonts=FONTS,
    words=("APPLE", "BANANA", "ORANGE", "PLANET", "GARDEN"),
    difficulty="easy",
    style="minimal",
)

root = tk.Tk()
root.title("MissingCharacterCaptcha practical example")
image = ImageTk.PhotoImage(Image.open(result.path))
tk.Label(root, image=image).pack()
tk.Label(root, text="Complete the familiar word:", font=("Segoe UI", 12)).pack(pady=6)
entry = tk.Entry(root, justify="center", font=("Segoe UI", 18), width=5)
entry.pack()
status = tk.StringVar()
tk.Label(root, textvariable=status, font=("Segoe UI", 12)).pack(pady=6)


def verify() -> None:
    status.set(
        "Solved!"
        if entry.get().strip().upper() == str(result.answer).upper()
        else "Try again."
    )


tk.Button(root, text="Verify", command=verify, width=16).pack(pady=10)
root.mainloop()
