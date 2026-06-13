from pathlib import Path
import sys
import tkinter as tk

from PIL import Image, ImageTk

sys.path.insert(0, str(Path(__file__).parents[1]))
from _shared import FONTS, output_dir
from CaptchaGenerator import CaptchaConfig, LogicChallengeCaptcha

result = LogicChallengeCaptcha(CaptchaConfig(width=900, height=300, random_seed=520)).generate(
    name_export="interactive_logic",
    path_export=str(output_dir(__file__)),
    fonts=FONTS,
    difficulty="medium",
)

root = tk.Tk()
root.title("LogicChallengeCaptcha")
photo = ImageTk.PhotoImage(Image.open(result.path))
tk.Label(root, image=photo).pack(padx=12, pady=12)
tk.Label(root, text=result.prompt, font=("Segoe UI", 12, "bold")).pack()
answer = tk.StringVar()
tk.Entry(root, textvariable=answer, font=("Segoe UI", 14), width=28).pack(pady=8)
status = tk.StringVar()
tk.Button(
    root, text="Verify",
    command=lambda: status.set(
        "Solved!" if answer.get().strip().casefold() == str(result.answer).casefold() else "Try again."
    ),
).pack()
tk.Label(root, textvariable=status).pack(pady=10)
root.mainloop()
