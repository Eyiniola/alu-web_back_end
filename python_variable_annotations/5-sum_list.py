#!/usr/bin/env python3
"""
This module defines a type-annotated function sum_list which calculates the
sum of a list of floats.
"""

from typing import List


def sum_list(input_list: List[float]) -> float:
    """
    Computes the sum of a list of floating-point numbers.

    Args:
        input_list (List[float]): A list of floating-point numbers.

    Returns:
        float: The sum of the numbers in the input list.
    """
    return sum(input_list)
