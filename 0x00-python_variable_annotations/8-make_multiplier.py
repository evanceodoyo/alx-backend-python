#!/usr/bin/env python3
"""Annotatated function that returns a callable"""
from typing import Callable


def make_multiplier(multiplier: float) -> Callable[[float], float]:
    """
    Returns a function that multiplies a float by the given multiplier.

    Parameters:
        multiplier (float): The multiplier to be used in the returned function.

    Returns:
        Callable[[float], float]: A function that takes a float and returns the
        result of multiplying that float by the given multiplier.
    """
    def multiplier_func(x: float) -> float:
        return x * multiplier

    return multiplier_func
