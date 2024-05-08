#!/usr/bin/env python3
"""More annotations and type checking using mypy"""
from typing import List, Tuple


def zoom_array(lst: Tuple, factor: int = 2) -> List:
    """
    Zooms in on the given tuple by duplicating each element a specified
    number of times.

    Parameters:
        lst (Tuple): The input tuple to be zoomed in.
        factor (int, optional): The zoom factor, indicating how many times
            each element should be duplicated. Defaults to 2.

    Returns:
        List: A list containing each element of the input tuple duplicated
            by the specified factor.
    """
    zoomed_in: List = [
        item for item in lst
        for i in range(int(factor))
    ]
    return zoomed_in


array = (12, 72, 91)

zoom_2x = zoom_array(array)

zoom_3x = zoom_array(array, 3)
