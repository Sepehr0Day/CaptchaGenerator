from __future__ import annotations

import random
from typing import Callable

from CaptchaGenerator.base import BaseCaptchaGenerator


class MathCaptcha(BaseCaptchaGenerator):
    """Generator for math-based captchas (e.g., '3 + 7')."""

    OPERATORS: tuple[str, ...] = ("+", "-", "*")
    MAX_OPERAND: int = 10

    def generate(self) -> tuple[str, int]:
        """Generate a math captcha and return the expression and result.

        Returns:
            A tuple containing (expression_string, integer_result).
        """
        num1 = random.randint(0, self.MAX_OPERAND)
        num2 = random.randint(0, self.MAX_OPERAND)
        operator = random.choice(self.OPERATORS)

        # Ensure subtraction results are non-negative
        if operator == "-" and num1 < num2:
            num1, num2 = num2, num1

        operator_functions: dict[str, Callable[[int, int], int]] = {
            "+": lambda x, y: x + y,
            "-": lambda x, y: x - y,
            "*": lambda x, y: x * y,
        }

        result = operator_functions[operator](num1, num2)
        expression = f"{num1} {operator} {num2}"

        return expression, result
