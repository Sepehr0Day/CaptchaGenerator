from pathlib import Path
import sys
import tkinter as tk

from PIL import Image, ImageTk

sys.path.insert(0, str(Path(__file__).parents[1]))
from _shared import output_dir
from CaptchaGenerator import CaptchaConfig, MazeCaptcha

config = CaptchaConfig(width=800, height=520, padding=24, random_seed=73)
result = MazeCaptcha(config).generate(
    name_export="interactive_maze",
    path_export=str(output_dir(__file__)),
    columns=10,
    rows=7,
    answer_mode="directions",
)

root = tk.Tk()
root.title("MazeCaptcha practical example")
maze_image = ImageTk.PhotoImage(Image.open(result.path))
canvas = tk.Canvas(root, width=config.width, height=config.height, highlightthickness=0)
canvas.pack()
canvas.create_image(0, 0, image=maze_image, anchor="nw")

columns = result.metadata["columns"]
rows = result.metadata["rows"]
cell_width = (config.width - config.padding * 2) / columns
cell_height = (config.height - config.padding * 2) / rows
current = list(result.metadata["start"])
step = 0


def center(cell: list[int]) -> tuple[float, float]:
    return (
        config.padding + (cell[0] + 0.5) * cell_width,
        config.padding + (cell[1] + 0.5) * cell_height,
    )


x, y = center(current)
player = canvas.create_oval(x - 8, y - 8, x + 8, y + 8, fill="#2563eb", outline="")
status = tk.StringVar(value="Move from S to E.")
tk.Label(root, textvariable=status, font=("Segoe UI", 12)).pack(pady=6)


def reset() -> None:
    global current, step
    current = list(result.metadata["start"])
    step = 0
    x, y = center(current)
    canvas.coords(player, x - 8, y - 8, x + 8, y + 8)


def move(direction: str) -> None:
    global step
    # Production clients submit moves; the server compares them with result.answer.
    if step >= len(result.answer):
        status.set("Already solved.")
        return
    if direction != result.answer[step]:
        status.set("Wrong turn. Restarted.")
        reset()
        return
    delta = {"up": (0, -1), "down": (0, 1), "left": (-1, 0), "right": (1, 0)}
    dx, dy = delta[direction]
    current[0] += dx
    current[1] += dy
    step += 1
    x, y = center(current)
    canvas.coords(player, x - 8, y - 8, x + 8, y + 8)
    status.set("Solved!" if step == len(result.answer) else f"Correct moves: {step}")


controls = tk.Frame(root)
controls.pack(pady=8)
tk.Button(controls, text="Up", width=9, command=lambda: move("up")).grid(row=0, column=1)
tk.Button(controls, text="Left", width=9, command=lambda: move("left")).grid(row=1, column=0)
tk.Button(controls, text="Down", width=9, command=lambda: move("down")).grid(row=1, column=1)
tk.Button(controls, text="Right", width=9, command=lambda: move("right")).grid(row=1, column=2)
tk.Button(controls, text="Reset", width=9, command=reset).grid(row=2, column=1)
root.mainloop()
