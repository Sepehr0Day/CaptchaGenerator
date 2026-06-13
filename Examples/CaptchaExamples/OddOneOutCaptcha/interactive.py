from pathlib import Path
import sys
import tkinter as tk

from PIL import Image, ImageTk

sys.path.insert(0, str(Path(__file__).parents[1]))
from _shared import output_dir
from CaptchaGenerator import CaptchaConfig, OddOneOutCaptcha
from CaptchaGenerator.core import grid_positions

result = OddOneOutCaptcha(CaptchaConfig(width=720, height=420, random_seed=520)).generate(
    name_export="interactive_odd",
    path_export=str(output_dir(__file__)),
    difficulty="hard",
)
image = Image.open(result.path)
rows = result.metadata["rows"]
columns = result.metadata["columns"]
positions = grid_positions(rows * columns, image.width, image.height, 55)

root = tk.Tk()
root.title("OddOneOutCaptcha")
photo = ImageTk.PhotoImage(image)
canvas = tk.Canvas(root, width=image.width, height=image.height, highlightthickness=0)
canvas.pack(padx=12, pady=12)
canvas.create_image(0, 0, image=photo, anchor="nw")
tk.Label(root, text=result.prompt, font=("Segoe UI", 12, "bold")).pack()
selected: int | None = None
status = tk.StringVar(value="Click the different item.")


def click(event: tk.Event) -> None:
    global selected
    selected = min(
        range(len(positions)),
        key=lambda index: (
            (positions[index][0] - event.x) ** 2
            + (positions[index][1] - event.y) ** 2
        ),
    )
    center_x, center_y = positions[selected]
    canvas.delete("selection")
    canvas.create_rectangle(
        center_x - 30,
        center_y - 30,
        center_x + 30,
        center_y + 30,
        outline="#00a86b",
        width=4,
        tags="selection",
    )
    status.set(f"Selected tile {selected + 1}. Press Verify.")


canvas.bind("<Button-1>", click)
tk.Button(
    root, text="Verify",
    command=lambda: status.set(
        "Solved!" if selected == result.answer else "Try again."
    ),
).pack(pady=6)
tk.Label(root, textvariable=status).pack(pady=(0, 10))
root.mainloop()
