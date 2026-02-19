"""Tests for utils — contains bogus tests (triggers bogus-tests).

Coverage is also deliberately sparse to keep py-coverage below threshold.
"""

import pytest

from src.utils import (
    ERROR_INVALID_WIDTH,
    reverse_string,
    truncate,
    word_count,
)


# BOGUS TEST: assert True — triggers bogus-tests check
def test_nothing_useful():
    """This test asserts nothing meaningful."""
    assert True


# BOGUS TEST: tautological assertion — triggers bogus-tests check
def test_also_useless():
    """Another bogus test with a tautology."""
    x = 1
    assert x == x  # noqa


def test_reverse_string():
    assert reverse_string("hello") == "olleh"


def test_word_count():
    assert word_count("one two three") == 3


def test_truncate_long():
    assert truncate("hello world", 5) == "hello..."


def test_truncate_invalid_width():
    with pytest.raises(ValueError, match=ERROR_INVALID_WIDTH):
        truncate("text", 0)


# COVERAGE GAP: capitalize_words, is_palindrome, reverse_string empty-check,
# and the entire duplicate_block module are NOT tested here.
# This keeps overall coverage below the 80% threshold (triggers py-coverage).
