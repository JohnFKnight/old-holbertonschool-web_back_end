#!/usr/bin/env python3

import unittest
from utils import access_nested_map
from parameterized import parameterized, parameterized_class


class TestAccessNestedMap(unittest.TestCase):
    """ Test Access Nested Map
    """
    # @parameterized_class(('nested', 'path', 'expected'), [
    #     ({"a": 1}, ("a",), 1),
    #     ({"a": {"b": 2}}, ("a", "b"), 2),
    #     ({"a": {"b": 2}}, ("a",), '{"b": 2}'),
    # ])
    @parameterized.expand([
        ({"a": 1}, ("a",), 1),
        ({"a": {"b": 2}}, ("a", "b"), 2),
        ({"a": {"b": 2}}, ("a",), {"b": 2}),
    ])
    def test_access_nested_map(self, nested, path, expected):
        """ Test access nested map function
        """
        self.assertEqual(access_nested_map(nested, path), expected)


if __name__ == "__main__":
    """ main """
    unittest.main()
