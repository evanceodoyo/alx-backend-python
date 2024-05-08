#!/usr/bin/env python3
"""Annotates result of floor() operation on float"""
import math


def floor(n: float) -> int:
    """
    Return the floor of the input number.

    Parameters:
        n (float): A floating-point number.

    Returns:
        float: The largest integer less than or equal to n.
    """
    return math.floor(n)
