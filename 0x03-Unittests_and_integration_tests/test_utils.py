#!/usr/bin/env python3
"""
Module for unit test for `utils` module.
"""
import unittest
from unittest.mock import Mock, patch
from functools import reduce
from typing import Dict, Tuple
from parameterized import parameterized, param

access_nested_map = __import__('utils').access_nested_map
get_json = __import__('utils').get_json
memoize = __import__('utils').memoize


class TestAccessNestedMap(unittest.TestCase):
    """
    Test class for `access_nested_map` function.
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


class TestGetJson(unittest.TestCase):
    """
    Test class for `get_json` function.
    """
    @parameterized.expand([
        param(test_url="http://example.com", test_payload={"payload": True}),
        param(test_url="http://holberton.io", test_payload={"payload": False}),
    ])
    def test_get_json(self, test_url: str, test_payload: Dict):
        """
        Test `get_json` output/return value.
        """
        attrs = {"json.return_value": test_payload}
        with patch("requests.get", return_value=Mock(**attrs)) as mock_req:
            self.assertEqual(get_json(test_url), test_payload)
            mock_req.assert_called_once_with(test_url)


class TestMemoize(unittest.TestCase):
    """
    Test class for `memoize` function.
    """
    def test_memoize(self):
        """
        Test output/return value of `memoize`
        """
        class TestClass:

            def a_method(self):
                return 42

            @memoize
            def a_property(self):
                return self.a_method()
        with patch.object(
            TestClass,
            "a_method",
            return_value=lambda: 42
        ) as memo_fn:
            test_cls = TestClass()
            self.assertEqual(test_cls.a_property(), 42)
            self.assertEqual(test_cls.a_property(), 42)
            memo_fn.assert_called_once()


if __name__ == '__main__':
    unittest.main()
