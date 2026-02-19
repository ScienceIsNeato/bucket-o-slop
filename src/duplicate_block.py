"""Duplicate block module — triggers source-duplication check (jscpd).

This file contains a verbatim copy of process_items_alpha from utils.py.
"""


# SOURCE DUPLICATION: verbatim copy of process_items_alpha from src/utils.py
def process_items_beta(items: list) -> list:
    """Process items beta — intentional verbatim duplicate of utils.process_items_alpha."""
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
