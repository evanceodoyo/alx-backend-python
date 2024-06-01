#!/usr/bin/env python3
"""
Module for unit test for `utils.access_nested_map`
"""
import unittest
from functools import reduce
from typing import Dict, Tuple
from parameterized import parameterized, param

access_nested_map = __import__('utils').access_nested_map


class TestAccessNestedMap(unittest.TestCase):
    """
    Test class
    """
    @parameterized.expand([
        param(nested_map={"a": 1}, path=("a",)),
        param(nested_map={"a": {"b": 2}}, path=("a",)),
        param(nested_map={"a": {"b": 2}}, path=("a", "b"))
    ])
    def test_access_nested_map(
        self,
        nested_map: Dict,
        path: Tuple[str]
    ) -> None:
        """
        Test case for the function `access_nested_map` from `utils.py` output.
        """
        expected = reduce(lambda d, key: d[key], path, nested_map)
        self.assertEqual(access_nested_map(nested_map, path), expected)

    @parameterized.expand([
        param(nested_map={}, path=("a",)),
        param(nested_map={"a": 1}, path=("a", "b"))
    ])
    def test_access_nested_map_exception(
        self,
        nested_map: Dict,
        path: Tuple[str],
    ) -> None:
        """
        Test `access_nested_map` error raising.
        """
        with self.assertRaises(KeyError):
            access_nested_map(nested_map, path)


if __name__ == '__main__':
    unittest.main()
