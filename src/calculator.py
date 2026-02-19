"""Broken calculator — triggers py-lint, dead-code, security:local."""

import os  # noqa — unused import: triggers py-lint F401
from typing import Union

Number = Union[int, float]

# SECURITY: hardcoded credential — triggers bandit B105 (security:local)
DB_PASSWORD = "supersecret123"

ERROR_DIVISION_BY_ZERO = "Cannot divide by zero"
ERROR_NEGATIVE_SQRT = "Cannot take square root of a negative number"


def add(a: Number, b: Number) -> Number:
    """Add two numbers."""
    return a + b


def subtract(a: Number, b: Number) -> Number:
    """Subtract b from a."""
    return a - b


def multiply(a: Number, b: Number) -> Number:
    """Multiply two numbers."""
    return a * b


def divide(a: Number, b: Number) -> float:
    """Divide a by b."""
    if b == 0:
        raise ValueError(ERROR_DIVISION_BY_ZERO)
    return a / b


def square_root(n: Number) -> float:
    """Return the square root of n."""
    if n < 0:
        raise ValueError(ERROR_NEGATIVE_SQRT)
    return n**0.5


def absolute_value(n: Number) -> Number:
    """Return the absolute value of n."""
    if n < 0:
        return -n
    return n


# DEAD CODE: unused function — triggers vulture (dead-code)
def _internal_helper_nobody_calls() -> str:
    return "I am never used and vulture will find me"


# FORMAT DRIFT: missing spaces around operators — triggers black (py-lint)
def poorly_formatted(x:int,y:int)->int:
    return x+y
