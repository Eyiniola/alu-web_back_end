#!/usr/bin/env python3
"""
Annotated functions parameters and return values with the appropriate types
"""

from typing import Iterable, Sequence, List, Tuple


def element_length(lst: Iterable[Sequence]) -> List[Tuple[Sequence, int]]:
    """
    Takes an iterable of sequences and returns a list of tuples where
    each tuple contains the sequence and its corresponding length.

    Args:
        lst (Iterable[Sequence]): An iterable of sequences (e.g., strings,
        lists).

    Returns:
        List[Tuple[Sequence, int]]: A list of tuples, each containing a
        sequence and its length.
    """
    return [(i, len(i)) for i in lst]
