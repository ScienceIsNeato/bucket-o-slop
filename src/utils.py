"""Text utilities module — clean code for happy-path testing."""

ERROR_EMPTY_STRING = "Input string cannot be empty"
ERROR_INVALID_WIDTH = "Width must be a positive integer"


def reverse_string(s: str) -> str:
    """Return the reversed version of s.

    Raises:
        ValueError: If s is empty.
    """
    if not s:
        raise ValueError(ERROR_EMPTY_STRING)
    return s[::-1]


def word_count(text: str) -> int:
    """Count words in text."""
    return len(text.split())


def truncate(text: str, width: int) -> str:
    """Truncate text to width characters, appending '...' if needed.

    Raises:
        ValueError: If width is not a positive integer.
    """
    if width <= 0:
        raise ValueError(ERROR_INVALID_WIDTH)
    if len(text) <= width:
        return text
    return text[:width] + "..."


def capitalize_words(text: str) -> str:
    """Capitalize the first letter of each word."""
    return " ".join(word.capitalize() for word in text.split())


def is_palindrome(s: str) -> bool:
    """Return True if s is a palindrome (case-insensitive)."""
    cleaned = s.lower().replace(" ", "")
    return cleaned == cleaned[::-1]
