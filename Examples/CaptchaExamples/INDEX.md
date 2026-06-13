# Example index

| Folder | Demonstrated settings |
|---|---|
| `TextCaptcha` | All 4 difficulties and all 5 styles |
| `TextRandomCaptcha` | Character pool, variants, hard/wave rendering |
| `WordCaptcha` | Word file, font size, difficulty and style |
| `MathCaptcha` | Multiple plain arithmetic challenges |
| `MathImageCaptcha` | Image math, difficulty and style |
| `AudioCaptcha` | Character pool, length and MP3 output |
| `AnimatedCaptcha` | GIF frames, length, difficulty and style |
| `ImageRandomCaptcha` | Source folder and selection count |
| `ImageDirectionCaptcha` | Direction image folder |
| `ImageGridCaptcha` | Target name, source folder and grid size |
| `RotateImageCaptcha` | Custom source image and canvas size |
| `UpsideDownObjectCaptcha` | Item count, rotation and generated arrows |
| `ShapeCountCaptcha` | All 4 difficulty levels |
| `OddOneOutCaptcha` | Hard grid challenge |
| `ClickPointCaptcha` | Target shape, click coordinates and tolerance |
| `ColorChallengeCaptcha` | High contrast and custom size |
| `MissingCharacterCaptcha` | Pool, length, difficulty and style |
| `SequenceCaptcha` | Hard sequence and minimal rendering |
| `LogicChallengeCaptcha` | Logic modes and custom canvas |
| `SliderPuzzleCaptcha` | Source image and difficulty |
| `IrregularPuzzleCaptcha` | Vertices, radius, tolerance and procedural image |
| `PatternCompletionCaptcha` | Pattern length and option count |
| `MazeCaptcha` | Directions, path and exit answer modes |
| `AnalogClockCaptcha` | Minute step, numbers, palette and line width |
| `Perspective3DCaptcha` | Labels, requested face and perspective skew |
| `CustomQuestionCaptcha` | Question collection and mixed answer types |
| `CaptchaConfig` | WEBP, quality, colors, fonts, hooks and accessibility |

Practical interactive Tkinter demos are also available:

- `SliderPuzzleCaptcha/interactive.py`
- `IrregularPuzzleCaptcha/interactive.py`
- `MazeCaptcha/interactive.py`
- `MissingCharacterCaptcha/interactive.py`

Run everything:

```powershell
python Examples/CaptchaExamples/run_all.py
```

Run without the network-dependent audio example:

```powershell
python Examples/CaptchaExamples/run_all.py --offline
```
