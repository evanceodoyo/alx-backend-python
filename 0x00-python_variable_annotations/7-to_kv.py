#!/usr/bin/env python3
"""Annotates mixed type - string and int/float"""
from typing import Tuple, Union


def to_kv(k: str, v: Union[int, float]) -> Tuple[str, float]:
    """
    Convert a 'key-value' pair into a tuple where the value is squared.

    Parameters:
        k (str): The key.
        v (Union[int, float]): The value, which can be an integer or a
        floating-point number.

    Returns:
        Tuple[str, float]: A tuple containing the key and the squared value.
    """
    return tuple([k, v ** 2])
