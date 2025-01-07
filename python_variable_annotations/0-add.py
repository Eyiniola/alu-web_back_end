#!/usr/bin/env python3
"""
This module provides a function that uses type annotations to
specify argument and return types.
"""


def add(a: float, b: float) -> float:
    """
    Adds two floating-point numbers and returns their sum.

    Args:
        a (float): The first floating-point number.
        b (float): The second floating-point number.

    Returns:
        float: The sum of the two numbers.
    """
    return a + b
