from pathlib import Path
import sys
import tkinter as tk

from PIL import Image, ImageTk

sys.path.insert(0, str(Path(__file__).parents[1]))
from _shared import ASSETS
from CaptchaGenerator import ImageDirectionCaptcha

folder = ASSETS / "direction_images"
filename, expected = ImageDirectionCaptcha().generate(folder_path=str(folder))

root = tk.Tk()
root.title("ImageDirectionCaptcha")
photo = ImageTk.PhotoImage(Image.open(folder / filename))
tk.Label(root, image=photo).pack(padx=12, pady=12)
tk.Label(root, text="Choose the direction.", font=("Segoe UI", 12, "bold")).pack()
selected = tk.StringVar()
frame = tk.Frame(root)
frame.pack(pady=8)
for index, direction in enumerate(("Up", "Down", "Left", "Right", "UpLeft", "UpRight", "DownLeft", "DownRight")):
    tk.Radiobutton(
        frame, text=direction, value=direction, variable=selected,
        indicatoron=False, width=12,
    ).grid(row=0, column=index, padx=4)
status = tk.StringVar()
tk.Button(
    root, text="Verify",
    command=lambda: status.set(
        "Solved!" if selected.get().casefold() == expected.casefold() else "Try again."
    ),
).pack()
tk.Label(root, textvariable=status).pack(pady=10)
root.mainloop()
