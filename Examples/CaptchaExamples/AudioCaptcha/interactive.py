from pathlib import Path
import os
import sys
import tkinter as tk

sys.path.insert(0, str(Path(__file__).parents[1]))
from _shared import VALUES, output_dir
from CaptchaGenerator import AudioCaptcha

# gTTS needs internet access. Install the optional dependency with:
# python -m pip install "CaptchaGenerator[audio]"
expected, audio_path = AudioCaptcha().generate(
    number_gen=6,
    values_captcha=VALUES,
    name_export="interactive_audio",
    path_export=str(output_dir(__file__)),
)

root = tk.Tk()
root.title("AudioCaptcha")
tk.Label(
    root,
    text="Play the audio and type the characters you hear.",
    font=("Segoe UI", 12, "bold"),
).pack(padx=24, pady=16)
tk.Button(root, text="Play audio", width=20, command=lambda: os.startfile(audio_path)).pack()
answer = tk.StringVar()
tk.Entry(root, textvariable=answer, font=("Segoe UI", 14), width=24).pack(pady=10)
status = tk.StringVar()
tk.Button(
    root,
    text="Verify",
    command=lambda: status.set(
        "Solved!" if answer.get().strip().casefold() == expected.casefold() else "Try again."
    ),
).pack()
tk.Label(root, textvariable=status).pack(pady=10)
root.mainloop()
