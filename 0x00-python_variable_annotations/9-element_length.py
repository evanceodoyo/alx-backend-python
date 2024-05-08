#!/usr/bin/env python3
"""Duck type an iterable object"""
from typing import List, Iterable, Sequence, Tuple


def element_length(lst: Iterable[Sequence]) -> List[Tuple[Sequence, int]]:
    """
    Gives the length of each element in the input iterable.

    Parameters:
        lst (Iterable[Sequence]): An iterable containing sequences.

    Returns:
        List[Tuple[Sequence, int]]: A list of tuples where each tuple contains
        a sequence from the input iterable and its corresponding length.
    """
    return [(i, len(i)) for i in lst]
