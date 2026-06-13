from pathlib import Path
import sys
import tkinter as tk

from PIL import Image, ImageTk

sys.path.insert(0, str(Path(__file__).parents[1]))
from _shared import FONTS, VALUES, output_dir
from CaptchaGenerator import CaptchaConfig, TextRandomCaptcha

output = output_dir(__file__)
expected, variants = TextRandomCaptcha(
    CaptchaConfig(width=720, height=240, random_seed=520)
).generate(
    number_gen=6,
    values_captcha=VALUES,
    number_variants=5,
    backgrounds=[],
    fonts=FONTS,
    name_export="interactive_random_text",
    path_export=str(output),
    difficulty="hard",
    style="wave",
)
root = tk.Tk()
root.title("TextRandomCaptcha")
photo = ImageTk.PhotoImage(Image.open(output / "interactive_random_text.png"))
tk.Label(root, image=photo).pack(padx=12, pady=12)
tk.Label(root, text="Select the exact text shown.", font=("Segoe UI", 12, "bold")).pack()
answer = tk.StringVar()
frame = tk.Frame(root)
frame.pack(pady=8)
for index, choice in enumerate(variants):
    tk.Radiobutton(
        frame, text=choice, value=choice, variable=answer,
        indicatoron=False, width=14,
    ).grid(row=index // 3, column=index % 3, padx=4, pady=4)
status = tk.StringVar()
tk.Button(
    root, text="Verify",
    command=lambda: status.set("Solved!" if answer.get() == expected else "Try again."),
).pack()
tk.Label(root, textvariable=status).pack(pady=10)
root.mainloop()
