from pathlib import Path
import sys
import tkinter as tk

from PIL import Image, ImageSequence, ImageTk

sys.path.insert(0, str(Path(__file__).parents[1]))
from _shared import FONTS, VALUES, output_dir
from CaptchaGenerator import AnimatedCaptcha, CaptchaConfig

result = AnimatedCaptcha(CaptchaConfig(width=720, height=240, random_seed=520)).generate(
    name_export="interactive_animated",
    path_export=str(output_dir(__file__)),
    fonts=FONTS,
    values=VALUES,
    length=6,
    difficulty="hard",
    frame_count=8,
)
source = Image.open(result.path)

root = tk.Tk()
root.title("AnimatedCaptcha")
frames = [
    ImageTk.PhotoImage(frame.copy().convert("RGBA"))
    for frame in ImageSequence.Iterator(source)
]
image_label = tk.Label(root)
image_label.pack(padx=12, pady=12)


def animate(index: int = 0) -> None:
    image_label.configure(image=frames[index])
    root.after(source.info.get("duration", 120), animate, (index + 1) % len(frames))


animate()
tk.Label(root, text=result.prompt, font=("Segoe UI", 12, "bold")).pack()
answer = tk.StringVar()
tk.Entry(root, textvariable=answer, font=("Segoe UI", 14), width=24).pack(pady=8)
status = tk.StringVar()
tk.Button(
    root,
    text="Verify",
    command=lambda: status.set(
        "Solved!" if answer.get().strip().casefold() == str(result.answer).casefold() else "Try again."
    ),
).pack()
tk.Label(root, textvariable=status).pack(pady=10)
root.mainloop()
