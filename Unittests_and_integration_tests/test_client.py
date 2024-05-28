#!/usr/bin/env python3
"""Test suite for Client"""

import unittest
from unittest.mock import patch
from parameterized import parameterized
from typing import Mapping, Sequence, Any, Dict, Callable
from client import GithubOrgClient


class TestGithubOrgClient(unittest.TestCase):
    """Test class for GithubOrgClient"""

    @parameterized.expand([
        ("google")
        ("abc")
    ])
    @patch('client.get_json')
    def test_org(self, org_name: Callable):
        """Test for GithubOrgClient"""

        client = GithubOrgClient(org_name)

        first_response = client.org

        second_response = client.org

        self.assertIs(first_response, second_response) 

if __name__ == '__main__':
    unittest.main()
