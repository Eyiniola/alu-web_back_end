#!/usr/bin/env python3
"""
This module provides a function to compute the floor of a float value.
"""

import math


def floor(n: float) -> int:
    """
    Compute the floor of a float.

    Args:
        n (float): The float value to process.

    Returns:
        int: The largest integer less than or equal to the input float.
    """
    return math.floor(n)
