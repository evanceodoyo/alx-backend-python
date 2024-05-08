#!/usr/bin/env python3
"""Annotates mixed list - list of ints and floats"""
from typing import List, Union


def sum_mixed_list(mxd_list: List[Union[int, float]]) -> float:
    """
    Return the sum of elements in the mixed-type input list.

    Parameters:
        mxd_list (List[Union[int, float]]): A list of integers and/or
        floating-point numbers.

    Returns:
        float: The sum of all elements in the input list.
    """
    return sum(mxd_list)
