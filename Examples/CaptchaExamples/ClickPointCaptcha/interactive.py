from pathlib import Path
import sys
import tkinter as tk

from PIL import Image, ImageTk

sys.path.insert(0, str(Path(__file__).parents[1]))
from _shared import output_dir
from CaptchaGenerator import CaptchaConfig, ClickPointCaptcha

result = ClickPointCaptcha(CaptchaConfig(width=720, height=420, random_seed=520)).generate(
    name_export="interactive_click_point",
    path_export=str(output_dir(__file__)),
    target="circle",
)
image = Image.open(result.path)

root = tk.Tk()
root.title("ClickPointCaptcha")
photo = ImageTk.PhotoImage(image)
canvas = tk.Canvas(root, width=image.width, height=image.height, highlightthickness=0)
canvas.pack(padx=12, pady=12)
canvas.create_image(0, 0, image=photo, anchor="nw")
tk.Label(root, text=result.prompt, font=("Segoe UI", 12, "bold")).pack()
selected = None
status = tk.StringVar(value="Click the requested object.")


def select(event: tk.Event) -> None:
    global selected
    selected = (event.x, event.y)
    canvas.delete("selection")
    canvas.create_oval(
        event.x - 8, event.y - 8, event.x + 8, event.y + 8,
        outline="#00a86b", width=4, tags="selection",
    )


def verify() -> None:
    if selected is None:
        status.set("Select a point first.")
        return
    x, y = result.answer
    tolerance = result.metadata["tolerance"]
    distance_squared = (selected[0] - x) ** 2 + (selected[1] - y) ** 2
    status.set("Solved!" if distance_squared <= tolerance ** 2 else "Try again.")


canvas.bind("<Button-1>", select)
tk.Button(root, text="Verify", width=18, command=verify).pack(pady=6)
tk.Label(root, textvariable=status).pack(pady=(0, 10))
root.mainloop()
