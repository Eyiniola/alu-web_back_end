#!/usr/bin/env python3
"""
Annotated functions parameters and return values with the appropriate types
"""

from typing import List, Tuple


def element_length(lst: List[str]) -> List[Tuple[str, int]]:
    """
    Takes a list of strings and returns a list of tuples where each tuple contains
    the string and its corresponding length.

    Args:
        lst (List[str]): A list of strings.

    Returns:
        List[Tuple[str, int]]: A list of tuples, each containing a string and its length.
    """
    return [(i, len(i)) for i in lst]
