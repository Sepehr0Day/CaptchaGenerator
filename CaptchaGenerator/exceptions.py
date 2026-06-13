from __future__ import annotations


class CaptchaError(Exception):
    """Base exception class for CaptchaGenerator."""


class InvalidArgumentError(CaptchaError):
    """Raised when an argument is missing or invalid."""
