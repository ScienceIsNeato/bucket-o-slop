"""Simple calculator module — clean code for happy-path testing."""

from typing import Union

Number = Union[int, float]

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
    """Divide a by b.

    Raises:
        ValueError: If b is zero.
    """
    if b == 0:
        raise ValueError(ERROR_DIVISION_BY_ZERO)
    return a / b


def square_root(n: Number) -> float:
    """Return the square root of n.

    Raises:
        ValueError: If n is negative.
    """
    if n < 0:
        raise ValueError(ERROR_NEGATIVE_SQRT)
    return n**0.5


def absolute_value(n: Number) -> Number:
    """Return the absolute value of n."""
    if n < 0:
        return -n
    return n
