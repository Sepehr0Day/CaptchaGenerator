from pathlib import Path
import sys
import tkinter as tk

from PIL import Image, ImageTk

sys.path.insert(0, str(Path(__file__).parents[1]))
from _shared import ASSETS, output_dir
from CaptchaGenerator import CaptchaConfig, RotateImageCaptcha

result = RotateImageCaptcha(CaptchaConfig(width=720, height=420, random_seed=520)).generate(
    image_path=str(ASSETS / "direction_images" / "test_Up.png"),
    name_export="interactive_rotate",
    path_export=str(output_dir(__file__)),
)
root = tk.Tk()
root.title("RotateImageCaptcha")
photo = ImageTk.PhotoImage(Image.open(result.path))
tk.Label(root, image=photo).pack(padx=12, pady=12)
tk.Label(root, text=result.prompt, font=("Segoe UI", 12, "bold")).pack()
answer = tk.StringVar()
frame = tk.Frame(root)
frame.pack(pady=8)
choices = (
    ("90° Clockwise", "clockwise"),
    ("90° Counterclockwise", "counterclockwise"),
    ("180°", "180"),
)
for index, (label, value) in enumerate(choices):
    tk.Radiobutton(
        frame, text=label, value=value, variable=answer,
        indicatoron=False, width=22,
    ).grid(row=0, column=index, padx=4)
status = tk.StringVar()


def verify() -> None:
    if not answer.get():
        status.set("Choose a rotation first.")
    elif answer.get() == result.answer:
        status.set("Solved!")
    else:
        status.set("That rotation will not make the image upright. Try again.")


tk.Button(
    root,
    text="Verify",
    command=verify,
).pack()
tk.Label(root, textvariable=status).pack(pady=10)
root.mainloop()
