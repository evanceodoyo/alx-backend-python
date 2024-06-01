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

    def test_public_repos_url(self) -> None:
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

    @patch("client.get_json")
    def test_public_repos(self, mock_get_payload: MagicMock) -> None:
        """
        Test that `GithubOrgClient.public_repos` returns the correct value.
        """
        test_payload = {
            "repos_url": "https://api.github.com/users/google/repos",
            "repos": [
                {
                    "id": 1936771,
                    "name": "truth",
                    "full_name": "google/truth",
                    "private": False,
                    "owner": {
                        "login": "google",
                        "id": 1342004,
                    },
                    "fork": False,
                    "url": "https://api.github.com/repos/google/truth",
                    "size": 35267,
                    "open_issues_count": 79,
                    "visibility": "public",
                    "forks": 254,
                    "default_branch": "master",
                },
                {
                    "id": 3248507,
                    "name": "ruby-openid-apps-discovery",
                    "full_name": "google/ruby-openid-apps-discovery",
                    "private": False,
                    "owner": {
                        "login": "google",
                        "id": 1342004,
                    },
                    "fork": False,
                    "url": "https://api.github.com/repos/google/"
                    "ruby-openid-apps-discovery",
                    "homepage": "",
                    "size": 176,
                    "open_issues_count": 2,
                    "visibility": "public",
                    "forks": 23,
                    "default_branch": "master",
                },
            ]
        }
        mock_get_payload.return_value = test_payload["repos"]
        with patch(
            "client.GithubOrgClient._public_repos_url",
            new_callable=PropertyMock,
        ) as mock_public_repos_url:
            mock_public_repos_url.return_value = test_payload["repos_url"]
            self.assertEqual(
                GithubOrgClient("google").public_repos(),
                [
                    "truth",
                    "ruby-openid-apps-discovery",
                ],
            )
            mock_public_repos_url.assert_called_once()
        mock_get_payload.assert_called_once()
