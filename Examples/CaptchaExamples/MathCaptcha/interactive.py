from pathlib import Path
import sys
import tkinter as tk

sys.path.insert(0, str(Path(__file__).parents[1]))
import _shared  # noqa: F401
from CaptchaGenerator import MathCaptcha

expression, expected = MathCaptcha().generate()
root = tk.Tk()
root.title("MathCaptcha")
tk.Label(root, text="Solve the expression", font=("Segoe UI", 12, "bold")).pack(
    padx=30, pady=(20, 8)
)
tk.Label(root, text=expression, font=("Segoe UI", 24)).pack(pady=8)
answer = tk.StringVar()
tk.Entry(root, textvariable=answer, font=("Segoe UI", 14), width=20).pack(pady=8)
status = tk.StringVar()
tk.Button(
    root, text="Verify",
    command=lambda: status.set(
        "Solved!" if answer.get().strip() == str(expected) else "Try again."
    ),
).pack()
tk.Label(root, textvariable=status).pack(pady=12)
root.mainloop()
