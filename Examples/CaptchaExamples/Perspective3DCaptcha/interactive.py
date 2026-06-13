from pathlib import Path
import sys
import tkinter as tk

from PIL import Image, ImageTk

sys.path.insert(0, str(Path(__file__).parents[1]))
from _shared import FONTS, output_dir
from CaptchaGenerator import CaptchaConfig, Perspective3DCaptcha

result = Perspective3DCaptcha(
    CaptchaConfig(width=720, height=480, fonts=tuple(FONTS), random_seed=520)
).generate(
    name_export="interactive_3d",
    path_export=str(output_dir(__file__)),
    labels=("1", "2", "3"),
    ask_face="right",
    skew=0.42,
)
root = tk.Tk()
root.title("Perspective3DCaptcha")
photo = ImageTk.PhotoImage(Image.open(result.path))
tk.Label(root, image=photo).pack(padx=12, pady=12)
tk.Label(root, text=result.prompt, font=("Segoe UI", 12, "bold")).pack()
selected = tk.StringVar()
frame = tk.Frame(root)
frame.pack(pady=8)
for index, choice in enumerate(("1", "2", "3")):
    tk.Radiobutton(
        frame, text=choice, value=choice, variable=selected,
        indicatoron=False, width=12,
    ).grid(row=0, column=index, padx=4)
status = tk.StringVar()
tk.Button(
    root, text="Verify",
    command=lambda: status.set(
        "Solved!" if selected.get() == str(result.answer) else "Try again."
    ),
).pack()
tk.Label(root, textvariable=status).pack(pady=10)
root.mainloop()
