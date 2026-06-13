# Practical interactive integration

The generated answer is server-side secret state. Do not send `result.answer`,
`target_x`, or the Maze solution to an untrusted client.

## Slider and irregular puzzles

Both generators now export:

```python
result.metadata["background_path"]
result.metadata["piece_path"]
result.metadata["piece_start_x"]
result.metadata["target_y"]
result.metadata["tolerance"]
```

Display the background, place the piece at its starting coordinate, and move it
horizontally with a slider or drag gesture. Send only the user's final x
coordinate to the server:

```python
solved = abs(user_x - result.answer) <= result.metadata["tolerance"]
```

Runnable desktop implementations:

- `SliderPuzzleCaptcha/interactive.py`
- `IrregularPuzzleCaptcha/interactive.py`

## Maze

Generate with `answer_mode="directions"`. The client sends each move or the
final move list to the server. The server compares it with `result.answer`.

Runnable implementation:

- `MazeCaptcha/interactive.py`

## Missing character

The default mode now removes a character from a familiar word. Supply your own
domain-specific dictionary:

```python
result = MissingCharacterCaptcha().generate(
    words=("APPLE", "BANANA", "ORANGE"),
    # other required arguments...
)
```

The old random-string behavior remains available through `random_mode=True`,
but it should be paired with answer options because the missing value cannot be
deduced from a random sequence.

Runnable implementation:

- `MissingCharacterCaptcha/interactive.py`
