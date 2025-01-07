#!/usr/bin/env python3
"""
Module to define a function that takes a key and a value,
calculates the square of the value, and returns a tuple of the key
and the squared value.

This function ensures that the squared value is returned as a float.
"""

from typing import Tuple, Union


def to_kv(k: str, v: Union[int, float]) -> Tuple[str, float]:
    """
    Takes a key (k) and a value (v), squares the value, and returns a tuple
    containing the key and the squared value as a float.

    Args:
        k (str): The key to be paired with the squared value.
        v (Union[int, float]): The value to be squared, which can be an integer
                                or a float.

    Returns:
        Tuple[str, float]: A tuple containing the key and the squared value
                            as a float.
    """
    return k, float(v**2)
