# CaptchaGenerator 2.0.0

Fast, modular CAPTCHA generation for Python with **26 ready-to-use challenges**.

## Install

```bash
pip install CaptchaGenerator
```

Audio support:

```bash
pip install "CaptchaGenerator[audio]"
```

## Quick Start

```python
from CaptchaGenerator import CaptchaConfig, TextCaptcha

config = CaptchaConfig(width=720, height=240, random_seed=42)

answer = TextCaptcha(config).generate(
    number_gen=6,
    values_captcha="ABCDEFGHJKLMNPQRSTUVWXYZ23456789",
    name_export="captcha",
    path_export="./output",
    fonts=[],
    colors=["navy", "darkred"],
    backgrounds=[],
    difficulty="medium",
    style="modern",
)

print(answer)
```

## Included CAPTCHAs

- **Text:** text, random text, words and missing characters
- **Logic:** math, sequences, custom questions and visual logic
- **Images:** grids, rotation, direction, upside-down objects and click points
- **Puzzles:** sliders, irregular pieces, patterns and mazes
- **Visual:** clocks, colors, shapes, odd-one-out and 3D perspective
- **Media:** animated and audio CAPTCHA

All generators are available through `CaptchaGenerator.SUPPORTED_CAPTCHAS`.

## Customization

Use `CaptchaConfig` to control dimensions, colors, fonts, output format,
quality, accessibility text, random seed and render hooks.

Visual challenges return a `ChallengeResult` containing:

- `path` - generated image
- `answer` - expected answer; keep it server-side
- `prompt` - user instruction
- `metadata` - integration data
- `accessibility_text` - accessible description

## Examples

Each CAPTCHA has standalone simple and Tkinter examples:

```text
Examples/CaptchaExamples/<CaptchaName>/
  simple.py
  interactive.py
```

## Security

Never expose answers, target coordinates or puzzle solutions to an untrusted
client. Validate responses on the server.

## License

MIT
