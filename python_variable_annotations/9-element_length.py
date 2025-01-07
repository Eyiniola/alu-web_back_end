#!/usr/bin/env python3
"""
Annotated functions parameters and return values with the appropriate types
"""

from typing import Iterable, Sequence, Tuple, List


def element_length(lst: Iterable[Sequence]) -> List[Tuple[Sequence, int]]:
    """
    Takes a list of strings and returns a list of tuples where each tuple contains
    the string and its corresponding length.

    Args:
        lst (List[str]): A list of strings.

    Returns:
        List[Tuple[str, int]]: A list of tuples, each containing a string and its length.
    """
    return [(i, len(i)) for i in lst]
