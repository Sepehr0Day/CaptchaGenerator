from pathlib import Path
import sys
import tkinter as tk

from PIL import Image, ImageTk

sys.path.insert(0, str(Path(__file__).parents[1]))
from _shared import ASSETS
from CaptchaGenerator import ImageRandomCaptcha

selected_file, expected, _extension, choices = ImageRandomCaptcha().generate(
    path_folder=str(ASSETS / "random_images"),
    number_random_select=4,
)

root = tk.Tk()
root.title("ImageRandomCaptcha")
photo = ImageTk.PhotoImage(Image.open(ASSETS / "random_images" / selected_file))
tk.Label(root, image=photo).pack(padx=12, pady=12)
tk.Label(root, text="Which object is shown?", font=("Segoe UI", 12, "bold")).pack()
answer = tk.StringVar()
frame = tk.Frame(root)
frame.pack(pady=8)
for index, choice in enumerate(choices):
    tk.Radiobutton(
        frame, text=choice, value=choice, variable=answer,
        indicatoron=False, width=14,
    ).grid(row=index // 4, column=index % 4, padx=4, pady=4)
status = tk.StringVar()
tk.Button(
    root, text="Verify",
    command=lambda: status.set(
        "Solved!" if answer.get().casefold() == expected.casefold() else "Try again."
    ),
).pack()
tk.Label(root, textvariable=status).pack(pady=10)
root.mainloop()
