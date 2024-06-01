#!/usr/bin/env python3
"""
Module for unit test for `utils.access_nested_map`
"""
import unittest
from functools import reduce
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
    def test_access_nested_map(self, nested_map, path):
        """
        Test case for the function access_nested_map from utils.py
        """
        expected = reduce(lambda d, key: d[key], path, nested_map)
        self.assertEqual(access_nested_map(nested_map, path), expected)


if __name__ == '__main__':
    unittest.main()
