#!/usr/bin/env python3
"""Annotates a 'complex type' - list of floats"""
from typing import List


def sum_list(input_list: List[float]) -> float:
    """
    Return the sum of elements in the input list.

    Parameters:
        input_list (List[float]): A list of floating-point numbers.

    Returns:
        float: The sum of all elements in the input list.
    """
    return sum(input_list)
