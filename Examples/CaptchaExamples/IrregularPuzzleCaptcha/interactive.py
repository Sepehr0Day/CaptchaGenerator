from pathlib import Path
import sys
import tkinter as tk

from PIL import Image, ImageTk

sys.path.insert(0, str(Path(__file__).parents[1]))
from _shared import output_dir
from CaptchaGenerator import CaptchaConfig, IrregularPuzzleCaptcha

config = CaptchaConfig(
    width=800,
    height=480,
    background_color="#eef2ff",
    accent_colors=(
        "#000000",
        "#3b82f6",
        "#fafafa",
        "#1c1c1c",
        "#8b5cf6",
    ),
    random_seed=520,
)
result = IrregularPuzzleCaptcha(config).generate(
    name_export="interactive_irregular",
    path_export=str(output_dir(__file__)),
    vertices=9,
    piece_radius=55,
    tolerance=90,
)

root = tk.Tk()
root.title("IrregularPuzzleCaptcha practical example")
background = ImageTk.PhotoImage(Image.open(result.metadata["background_path"]))
piece = ImageTk.PhotoImage(Image.open(result.metadata["piece_path"]))
radius = result.metadata["piece_radius"]

canvas = tk.Canvas(root, width=config.width, height=config.height, highlightthickness=0)
canvas.pack()
canvas.create_image(0, 0, image=background, anchor="nw")
piece_item = canvas.create_image(
    result.metadata["piece_start_x"] - radius,
    result.metadata["target_y"] - radius,
    image=piece,
    anchor="nw",
)

status = tk.StringVar(value=result.prompt)
tk.Label(root, textvariable=status, font=("Segoe UI", 12)).pack(pady=6)


def move_piece(value: str) -> None:
    center_x = int(float(value))
    canvas.coords(
        piece_item,
        center_x - radius,
        result.metadata["target_y"] - radius,
    )


slider = tk.Scale(
    root,
    from_=radius,
    to=config.width - radius,
    orient="horizontal",
    length=config.width - 40,
    command=move_piece,
)
slider.set(result.metadata["piece_start_x"])
slider.pack()


def verify() -> None:
    distance = abs(slider.get() - result.answer)
    status.set("Solved!" if distance <= result.metadata["tolerance"] else "Try again.")


tk.Button(root, text="Verify", command=verify, width=18).pack(pady=10)
root.mainloop()
