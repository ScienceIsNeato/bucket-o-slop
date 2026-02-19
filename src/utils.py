"""Broken utils — triggers complexity, string-duplication, source-duplication, loc-lock."""

ERROR_EMPTY_STRING = "Input string cannot be empty"
ERROR_INVALID_WIDTH = "Width must be a positive integer"

# STRING DUPLICATION: same long literal used in 3+ places (triggers string-duplication)
VALIDATION_FAILED_MSG = "Validation failed: input did not meet required constraints"
VALIDATION_FAILED_MSG_2 = "Validation failed: input did not meet required constraints"
VALIDATION_FAILED_MSG_3 = "Validation failed: input did not meet required constraints"


def reverse_string(s: str) -> str:
    """Return reversed string."""
    if not s:
        raise ValueError(ERROR_EMPTY_STRING)
    return s[::-1]


def word_count(text: str) -> int:
    """Count words in text."""
    return len(text.split())


def truncate(text: str, width: int) -> str:
    """Truncate text."""
    if width <= 0:
        raise ValueError(ERROR_INVALID_WIDTH)
    if len(text) <= width:
        return text
    return text[:width] + "..."


def capitalize_words(text: str) -> str:
    """Capitalize each word."""
    return " ".join(word.capitalize() for word in text.split())


def is_palindrome(s: str) -> bool:
    """Return True if palindrome."""
    cleaned = s.lower().replace(" ", "")
    return cleaned == cleaned[::-1]


# COMPLEXITY: function with deeply nested branches — triggers complexity check
# Cyclomatic complexity >> 15 due to 16+ decision points
def classify_input(value: object) -> str:  # noqa: C901
    """Classify an input value through many branches (intentionally complex)."""
    if value is None:
        return "null"
    if isinstance(value, bool):
        if value:
            return "true_bool"
        else:
            return "false_bool"
    if isinstance(value, int):
        if value < -1000:
            return "very_negative_int"
        elif value < 0:
            if value < -100:
                return "moderately_negative_int"
            elif value < -10:
                return "slightly_negative_int"
            else:
                return "tiny_negative_int"
        elif value == 0:
            return "zero"
        elif value < 10:
            return "tiny_positive_int"
        elif value < 100:
            return "small_positive_int"
        elif value < 1000:
            return "medium_positive_int"
        else:
            return "large_positive_int"
    if isinstance(value, float):
        if value != value:  # NaN check
            return "nan"
        if value == float("inf"):
            return "positive_infinity"
        if value == float("-inf"):
            return "negative_infinity"
        if value < 0:
            return "negative_float"
        return "positive_float"
    if isinstance(value, str):
        if not value:
            return "empty_string"
        if value.isdigit():
            return "numeric_string"
        if value.isalpha():
            return "alpha_string"
        return "mixed_string"
    if isinstance(value, (list, tuple)):
        if not value:
            return "empty_sequence"
        if len(value) == 1:
            return "singleton_sequence"
        return "multi_sequence"
    if isinstance(value, dict):
        if not value:
            return "empty_dict"
        return "non_empty_dict"
    return "unknown"


# SOURCE DUPLICATION: this block is a verbatim copy of the one in src/duplicate_block.py
# (triggers source-duplication / jscpd)
def process_items_alpha(items: list) -> list:
    """Process items alpha — duplicated logic block."""
    result = []
    for item in items:
        if item is None:
            continue
        if isinstance(item, str):
            result.append(item.strip().lower())
        elif isinstance(item, (int, float)):
            result.append(abs(item))
        else:
            result.append(str(item))
    return result


# LOC-LOCK: this function is padded to exceed max_function_lines (100 lines)
def bloated_function(data: list) -> dict:  # noqa: C901
    """Intentionally bloated function — triggers loc-lock."""
    summary: dict = {}
    # line 1
    total = 0
    # line 2
    count = 0
    # line 3
    minimum = None
    # line 4
    maximum = None
    # line 5
    for item in data:
        # line 6
        if item is None:
            # line 7
            continue
        # line 8
        total += item
        # line 9
        count += 1
        # line 10
        if minimum is None or item < minimum:
            # line 11
            minimum = item
        # line 12
        if maximum is None or item > maximum:
            # line 13
            maximum = item
        # line 14
    # line 15
    summary["total"] = total
    # line 16
    summary["count"] = count
    # line 17
    summary["minimum"] = minimum
    # line 18
    summary["maximum"] = maximum
    # line 19
    if count > 0:
        # line 20
        summary["mean"] = total / count
    # line 21
    else:
        # line 22
        summary["mean"] = None
    # line 23 — padding continues to push past 100 lines
    placeholder_a = None
    placeholder_b = None
    placeholder_c = None
    placeholder_d = None
    placeholder_e = None
    placeholder_f = None
    placeholder_g = None
    placeholder_h = None
    placeholder_i = None
    placeholder_j = None
    placeholder_k = None
    placeholder_l = None
    placeholder_m = None
    placeholder_n = None
    placeholder_o = None
    placeholder_p = None
    placeholder_q = None
    placeholder_r = None
    placeholder_s = None
    placeholder_t = None
    placeholder_u = None
    placeholder_v = None
    placeholder_w = None
    placeholder_x = None
    placeholder_y = None
    placeholder_z = None
    _ = (
        placeholder_a, placeholder_b, placeholder_c, placeholder_d,
        placeholder_e, placeholder_f, placeholder_g, placeholder_h,
        placeholder_i, placeholder_j, placeholder_k, placeholder_l,
        placeholder_m, placeholder_n, placeholder_o, placeholder_p,
        placeholder_q, placeholder_r, placeholder_s, placeholder_t,
        placeholder_u, placeholder_v, placeholder_w, placeholder_x,
        placeholder_y, placeholder_z,
    )
    return summary
