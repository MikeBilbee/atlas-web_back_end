#!/usr/bin/env python3
"""
Test Suite for Utils, Client, & Fixtures
"""

import unittest
import parameterized
from utils import access_nested_map


class TestAccessNestedMap(unittest.TestCase):
    """Test class for AccessNestedMap"""

    @parameterized.expand([
        ({"a": 1}, ("a",), 1),
        ({"a": {"b": 2}}, ("a",), {"b": 2}),
        ({"a": {"b": 2}}, ("a", "b"), 2)
    ])
    def test_access_nested_map(self, nested_map, path, expected):
        """Test for AccessNestedMap"""

        result = access_nested_map(nested_map, path)
        self.assertEqual(result, expected)

if __name__ == '__main__':
    unittest.main()