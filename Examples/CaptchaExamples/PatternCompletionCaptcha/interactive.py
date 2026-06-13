from pathlib import Path
import sys
import tkinter as tk

from PIL import Image, ImageTk

sys.path.insert(0, str(Path(__file__).parents[1]))
from _shared import output_dir
from CaptchaGenerator import CaptchaConfig, PatternCompletionCaptcha

result = PatternCompletionCaptcha(
    CaptchaConfig(width=900, height=480, random_seed=520)
).generate(
    name_export="interactive_pattern",
    path_export=str(output_dir(__file__)),
    pattern_length=8,
    option_count=4,
)
image = Image.open(result.path)
root = tk.Tk()
root.title("PatternCompletionCaptcha")
photo = ImageTk.PhotoImage(image)
canvas = tk.Canvas(
    root,
    width=image.width,
    height=image.height,
    highlightthickness=0,
)
canvas.pack(padx=12, pady=12)
canvas.create_image(0, 0, image=photo, anchor="nw")
tk.Label(root, text=result.prompt, font=("Segoe UI", 12, "bold")).pack()
selected = tk.IntVar(value=-1)
option_count = len(result.metadata["options"])
padding = 24
usable_width = image.width - padding * 2
option_spacing = usable_width / option_count
option_y = int(image.height * 0.72)
status = tk.StringVar(value="Click one of the numbered shapes.")


def select_option(index: int) -> None:
    selected.set(index)
    center_x = int(padding + option_spacing * (index + 0.5))
    canvas.delete("selection")
    canvas.create_rectangle(
        center_x - option_spacing * 0.34,
        option_y - 65,
        center_x + option_spacing * 0.34,
        option_y + 75,
        outline="#00a86b",
        width=5,
        tags="selection",
    )
    status.set(f"Option {index + 1} selected. Press Verify.")


def click(event: tk.Event) -> None:
    if event.y < image.height * 0.55:
        return
    index = int((event.x - padding) / option_spacing)
    if 0 <= index < option_count:
        select_option(index)


def verify() -> None:
    if selected.get() < 0:
        status.set("Select one of the shapes first.")
    elif selected.get() == result.answer:
        status.set("Solved!")
    else:
        status.set("That shape does not complete the pattern. Try again.")


canvas.bind("<Button-1>", click)
tk.Button(
    root,
    text="Verify",
    command=verify,
).pack()
tk.Label(root, textvariable=status).pack(pady=10)
root.mainloop()
