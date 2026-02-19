"""Tests for the utils module."""

import pytest

from src.utils import (
    ERROR_EMPTY_STRING,
    ERROR_INVALID_WIDTH,
    capitalize_words,
    is_palindrome,
    reverse_string,
    truncate,
    word_count,
)


def test_reverse_string():
    assert reverse_string("hello") == "olleh"


def test_reverse_string_empty():
    with pytest.raises(ValueError, match=ERROR_EMPTY_STRING):
        reverse_string("")


def test_word_count():
    assert word_count("one two three") == 3


def test_word_count_single():
    assert word_count("hello") == 1


def test_truncate_short():
    assert truncate("hi", 10) == "hi"


def test_truncate_long():
    assert truncate("hello world", 5) == "hello..."


def test_truncate_invalid_width():
    with pytest.raises(ValueError, match=ERROR_INVALID_WIDTH):
        truncate("text", 0)


def test_capitalize_words():
    assert capitalize_words("hello world") == "Hello World"


def test_is_palindrome_true():
    assert is_palindrome("racecar") is True


def test_is_palindrome_false():
    assert is_palindrome("hello") is False


def test_is_palindrome_with_spaces():
    assert is_palindrome("race car") is True
