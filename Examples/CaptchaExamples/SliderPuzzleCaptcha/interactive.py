from pathlib import Path
import sys
import tkinter as tk

from PIL import Image, ImageTk

sys.path.insert(0, str(Path(__file__).parents[1]))
from _shared import ASSETS, output_dir
from CaptchaGenerator import CaptchaConfig, SliderPuzzleCaptcha

config = CaptchaConfig(width=720, height=420, random_seed=71)
result = SliderPuzzleCaptcha(config).generate(
    image_path=str(ASSETS / "random_images" / "Apple.png"),
    name_export="interactive_slider",
    path_export=str(output_dir(__file__)),
    difficulty="medium",
    tolerance=10,
)

root = tk.Tk()
root.title("SliderPuzzleCaptcha practical example")
background = ImageTk.PhotoImage(Image.open(result.metadata["background_path"]))
piece = ImageTk.PhotoImage(Image.open(result.metadata["piece_path"]))

canvas = tk.Canvas(root, width=config.width, height=config.height, highlightthickness=0)
canvas.pack()
canvas.create_image(0, 0, image=background, anchor="nw")
piece_item = canvas.create_image(
    result.metadata["piece_start_x"],
    result.metadata["target_y"],
    image=piece,
    anchor="nw",
)

status = tk.StringVar(value=result.prompt)
tk.Label(root, textvariable=status, font=("Segoe UI", 12)).pack(pady=6)


def move_piece(value: str) -> None:
    canvas.coords(piece_item, int(float(value)), result.metadata["target_y"])


slider = tk.Scale(
    root,
    from_=0,
    to=config.width - result.metadata["piece_size"],
    orient="horizontal",
    length=config.width - 40,
    command=move_piece,
)
slider.set(result.metadata["piece_start_x"])
slider.pack()


def verify() -> None:
    # In production, send slider.get() to the server. Keep result.answer server-side.
    distance = abs(slider.get() - result.answer)
    status.set("Solved!" if distance <= result.metadata["tolerance"] else "Try again.")


tk.Button(root, text="Verify", command=verify, width=18).pack(pady=10)
root.mainloop()
