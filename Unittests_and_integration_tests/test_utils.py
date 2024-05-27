#!/usr/bin/env python3
"""
Test Suite for Utils, Client, & Fixtures
"""

import unittest
from unittest.mock import patch
from parameterized import parameterized
from utils import access_nested_map, get_json, memoize
from typing import Mapping, Sequence, Any, Dict, Callable


class TestAccessNestedMap(unittest.TestCase):
    """Test class for AccessNestedMap"""

    @parameterized.expand([
        ({"a": 1}, ("a",), 1),
        ({"a": {"b": 2}}, ("a",), {"b": 2}),
        ({"a": {"b": 2}}, ("a", "b"), 2)
    ])
    def test_access_nested_map(self,
                               nested_map: Mapping,
                               path: Sequence,
                               expected: Any):
        """Test for AccessNestedMap"""

        self.assertEqual(access_nested_map(nested_map, path), expected)

    @parameterized.expand([
        ({}, ("a",), "a"),
        ({"a": 1}, ("a", "b"), "b")
    ])
    def test_access_nested_map_exception(self,
                                         nested_map: Mapping,
                                         path: Sequence,
                                         expected: Any):
        """Exception test for AccessNestedMap"""

        with self.assertRaises(KeyError) as context:
            access_nested_map(nested_map, path)

        self.assertEqual(context.exception.args[0], expected)


class TestGetJson(unittest.TestCase):
    """Test class for GetJson"""

    @parameterized.expand([
        ("http://example.com", {"payload": True}),
        ("http://holberton.io", {"payload": False})
    ])
    @patch('requests.get')
    def test_get_json(self,
                      test_url: str,
                      test_payload: Dict,
                      get_mock: Callable):
        """Test for GetJason"""
        get_mock.return_value.json.return_value = test_payload
        output = get_json(test_url)
        get_mock.assert_called_once_with(test_url)
        self.assertEqual(output, test_payload)


class TestMemoize(unittest.TestCase):
    """Test class for Memoize"""

    def test_memoize(self):
        """Test for Memoize"""

        class TestClass:
            """Test class"""

            def a_method(self):
                """A test method"""
                return 42

        @memoize
        def a_property(self):
            """A test property"""

            return self.a_method()

        obj = TestClass()

        with patch.object(obj, 'a_method') as mock_method:
            mock_method.return_value = 42

            result1 = obj.a_property
            result2 = obj.a_property

            self.assertEqual(result1, 42)
            self.assertEqual(result2, 42)
            mock_method.assert_called_once()


if __name__ == '__main__':
    unittest.main()
