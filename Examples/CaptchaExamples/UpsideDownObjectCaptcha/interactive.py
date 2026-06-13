from pathlib import Path
import sys
import tkinter as tk

from PIL import Image, ImageTk

sys.path.insert(0, str(Path(__file__).parents[1]))
from _shared import output_dir
from CaptchaGenerator import CaptchaConfig, UpsideDownObjectCaptcha

result = UpsideDownObjectCaptcha(
    CaptchaConfig(width=800, height=480, random_seed=520)
).generate(
    name_export="interactive_upside_down",
    path_export=str(output_dir(__file__)),
    item_count=12,
    rotation=180,
)
root = tk.Tk()
root.title("UpsideDownObjectCaptcha")
photo = ImageTk.PhotoImage(Image.open(result.path))
tk.Label(root, image=photo).pack(padx=12, pady=12)
tk.Label(root, text=result.prompt, font=("Segoe UI", 12, "bold")).pack()
selected = tk.IntVar(value=-1)
options = tk.Frame(root)
options.pack(pady=8)
for index in range(result.metadata["item_count"]):
    tk.Radiobutton(
        options,
        text=str(index + 1),
        value=index,
        variable=selected,
        indicatoron=False,
        width=5,
    ).grid(row=index // 6, column=index % 6, padx=3, pady=3)
status = tk.StringVar(value="Choose the number below the upside-down object.")
tk.Button(
    root, text="Verify",
    command=lambda: status.set(
        "Solved!" if selected.get() == result.answer else "Try again."
    ),
).pack(pady=6)
tk.Label(root, textvariable=status).pack(pady=(0, 10))
root.mainloop()
