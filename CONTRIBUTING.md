# Contributing

1. Fork the repository and create a focused branch.
2. Install development dependencies with `pip install -e ".[dev,audio]"`.
3. Add or update tests for behavioral changes.
4. Run `python -m pytest -q` and `python -m ruff check .`.
5. Open a pull request with a clear description and example output.

Keep generators modular and place shared rendering utilities in
`CaptchaGenerator/core`.
