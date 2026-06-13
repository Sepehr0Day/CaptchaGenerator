from __future__ import annotations

import subprocess
import sys
from pathlib import Path

ROOT = Path(__file__).parent
SKIP = {"AudioCaptcha"} if "--offline" in sys.argv else set()

failures = []
for script in sorted(ROOT.glob("*/simple.py")):
    if script.parent.name in SKIP:
        print(f"SKIP {script.parent.name} (offline mode)")
        continue
    print(f"RUN  {script.parent.name}")
    result = subprocess.run([sys.executable, str(script)], cwd=ROOT.parents[1])
    if result.returncode:
        failures.append(script.parent.name)

if failures:
    raise SystemExit(f"Failed examples: {', '.join(failures)}")
print("All examples completed successfully.")
