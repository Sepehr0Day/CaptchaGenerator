from pathlib import Path
import sys
import tkinter as tk

from PIL import Image, ImageTk

sys.path.insert(0, str(Path(__file__).parents[1]))
from _shared import ASSETS, output_dir
from CaptchaGenerator import CaptchaConfig, ImageGridCaptcha

size = 3
result = ImageGridCaptcha(CaptchaConfig(width=720, height=720, random_seed=520)).generate(
    path_folder=str(ASSETS / "random_images"),
    target_name="Tree",
    name_export="interactive_grid",
    path_export=str(output_dir(__file__)),
    grid_size=size,
)
image = Image.open(result.path)

root = tk.Tk()
root.title("ImageGridCaptcha")
photo = ImageTk.PhotoImage(image)
canvas = tk.Canvas(root, width=image.width, height=image.height, highlightthickness=0)
canvas.pack(padx=12, pady=12)
canvas.create_image(0, 0, image=photo, anchor="nw")
tk.Label(root, text=result.prompt, font=("Segoe UI", 12, "bold")).pack()
selected: set[int] = set()
status = tk.StringVar(value="Click every matching tile.")


def click(event: tk.Event) -> None:
    column = min(size - 1, int(event.x / (image.width / size)))
    row = min(size - 1, int(event.y / (image.height / size)))
    index = row * size + column
    selected.symmetric_difference_update({index})
    canvas.delete("selection")
    for item in selected:
        item_row, item_column = divmod(item, size)
        x1 = item_column * image.width / size
        y1 = item_row * image.height / size
        canvas.create_rectangle(
            x1 + 3, y1 + 3, x1 + image.width / size - 3,
            y1 + image.height / size - 3, outline="#00a86b",
            width=5, tags="selection",
        )


canvas.bind("<Button-1>", click)
tk.Button(
    root, text="Verify",
    command=lambda: status.set(
        "Solved!" if selected == set(result.answer) else "Try again."
    ),
).pack(pady=6)
tk.Label(root, textvariable=status).pack(pady=(0, 10))
root.mainloop()
