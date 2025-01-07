#!/usr/bin/env python3
"""
This module defines a type-annotated function `sum_mixed_list` that calculates
the sum of a list containing both integers and floats.
"""

from typing import List, Union


def sum_mixed_list(mxd_lst: List[Union[int, float]]) -> float:
    """
    Computes the sum of a list containing both integers and floating-point
    numbers.

    Args:
        mxd_lst (List[Union[int, float]]): A list of integers and/or floats.

    Returns:
        float: The sum of the numbers in the input list as a floating-point
        number.
    """
    return sum(mxd_lst)
