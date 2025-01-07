#!/usr/bin/env python3
"""
Returns a function that multiplies a float by the given multiplier.
"""

from typing import Callable


def make_multiplier(multiplier: float) -> Callable[[float], float]:
    """
    Takes a multiplier and returns a function that multiplies a float by it.

    Args:
        multiplier (float): The value to multiply the input by.

    Returns:
        Callable[[float], float]: A function that takes a float as input
                                  and returns the product of the input
                                  and multiplier.
    """
    def multiply(value: float) -> float:
        return value * multiplier
    return multiply
