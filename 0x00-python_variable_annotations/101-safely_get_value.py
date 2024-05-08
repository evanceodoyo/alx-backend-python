#!/usr/bin/env python3
"""Demonstrate how to use TypeVar"""
from typing import Any, Mapping, Union, TypeVar

T = TypeVar('T')


def safely_get_value(dct: Mapping, key: Any, default: Union[T, None]) -> \
        Union[Any, T]:
    """
    Retrieves the value associated with the given key from the dictionary.

    Parameters:
        dct (Mapping): A mapping containing key-value pairs.
        key (Any): The key whose value is to be retrieved.
        default (Union[T, None]): Default value if the key is not found.

    Returns:
        Union[Any, T]: Value associated with the key or the default value.
    """
    if key in dct:
        return dct[key]
    else:
        return default
