"""Tests for utils — contains bogus tests (triggers bogus-tests).

Coverage is also deliberately sparse to keep py-coverage below threshold.
"""

import pytest

from src.utils import (
    ERROR_EMPTY_STRING,
    ERROR_INVALID_WIDTH,
    reverse_string,
    truncate,
    word_count,
)


def test_reverse_string_empty():
    with pytest.raises(ValueError, match=ERROR_EMPTY_STRING):
        reverse_string("")


def test_word_count_single_word():
    assert word_count("hello") == 1


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
