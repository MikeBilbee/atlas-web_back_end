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
    def test_org(self, org_name, mock_get_json):
        """Test for GithubOrgClient"""

        test_client = GithubOrgClient(org_name)

        test_client.org()

        mock_get_json.assert_called_once_with(
            f"https://api.github.com/orgs/{org_name}")

if __name__ == '__main__':
    unittest.main()
