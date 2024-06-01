#!/usr/bin/env python3
"""
Module for unit test for `client` module.
"""
import unittest
from unittest.mock import MagicMock, PropertyMock, patch
from typing import Dict
from parameterized import parameterized


GithubOrgClient = __import__('client').GithubOrgClient
# from client import GithubOrgClient


class TestGithubOrgClient(unittest.TestCase):
    """
    Test class for `client` module.
    """
    @parameterized.expand([
        ("google", {"login": "google", "id": 1, "type": "Organization"}),
        ("abc", {"login": "abc", "id": 2, "type": "Organization"})
    ])
    @patch("client.get_json")
    def test_org(self, org: str, resp: Dict, mock_get: MagicMock) -> None:
        """
        Test that `GithubOrgClient.org` returns the correct value.
        """
        mock_get.return_value = MagicMock(return_value=resp)
        ghorg_client_obj = GithubOrgClient(org)
        self.assertEqual(ghorg_client_obj.org(), resp)
        mock_get.assert_called_once_with(f"https://api.github.com/orgs/{org}")

    def test_public_repos_url(self):
        """
        Test that `GithubOrgClient._public_repos_url`
        returns the correct value.
        """
        with patch(
            "client.GithubOrgClient.org",
            new_callable=PropertyMock
        ) as mock_org:
            mock_org.return_value = {
                "repos_url": "https://api.github.com/orgs/google/repos"
            }
            self.assertEqual(
                GithubOrgClient("google")._public_repos_url,
                "https://api.github.com/orgs/google/repos"
            )
