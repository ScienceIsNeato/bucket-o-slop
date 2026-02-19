"""Tests for the calculator module."""

import pytest

from src.calculator import (
    ERROR_DIVISION_BY_ZERO,
    ERROR_NEGATIVE_SQRT,
    absolute_value,
    add,
    divide,
    multiply,
    square_root,
    subtract,
)


def test_add_positive():
    assert add(2, 3) == 5


def test_add_negative():
    assert add(-1, -4) == -5


def test_add_mixed():
    assert add(-1, 3) == 2


def test_subtract():
    assert subtract(10, 4) == 6


def test_subtract_negative_result():
    assert subtract(3, 10) == -7


def test_multiply():
    assert multiply(4, 5) == 20


def test_multiply_by_zero():
    assert multiply(7, 0) == 0


def test_divide_basic():
    assert divide(10, 2) == 5.0


def test_divide_by_zero():
    with pytest.raises(ValueError, match=ERROR_DIVISION_BY_ZERO):
        divide(5, 0)


def test_square_root():
    assert square_root(9) == 3.0


def test_square_root_negative():
    with pytest.raises(ValueError, match=ERROR_NEGATIVE_SQRT):
        square_root(-1)


def test_absolute_value_positive():
    assert absolute_value(5) == 5


def test_absolute_value_negative():
    assert absolute_value(-3) == 3


def test_absolute_value_zero():
    assert absolute_value(0) == 0


# BOGUS TEST: tautological assertion — triggers bogus-tests check
def test_bogus_always_passes():
    x = absolute_value(3)
    assert x == x  # no real assertion
