#!/usr/bin/env python3
"""
Module for unit test for `client` module.
"""
import unittest
from requests import HTTPError
from unittest.mock import MagicMock, Mock, PropertyMock, patch
from typing import Dict
from parameterized import parameterized, parameterized_class
from fixtures import TEST_PAYLOAD


GithubOrgClient = __import__('client').GithubOrgClient


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

    @parameterized.expand([
        ({"license": {"key": "my_license"}}, "my_license", True),
        ({"license": {"key": "other_license"}}, "my_license", False)
    ])
    def test_has_license(self, repo: Dict, key: str, expected: bool) -> None:
        """
        Test that `GithubOrgClient.has_license` returns the correct value.
        """
        ghorg_client_obj = GithubOrgClient("my-org")
        has_license = ghorg_client_obj.has_license(repo, key)
        self.assertEqual(has_license, expected)


@parameterized_class([
    {
        "org_payload": TEST_PAYLOAD[0][0],
        "repos_payload": TEST_PAYLOAD[0][1],
        "expected_repos": TEST_PAYLOAD[0][2],
        "apache2_repos": TEST_PAYLOAD[0][3],
    }
])
class TestIntegrationGithubOrgClient(unittest.TestCase):
    """
    Integration test class for `GithubOrgClient`.
    """
    @classmethod
    def setUpClass(cls) -> None:
        """Set up class before running tests"""
        route_payload = {
            'https://api.github.com/orgs/google': cls.org_payload,
            'https://api.github.com/orgs/google/repos': cls.repos_payload,
        }

        def get_payload(url):
            if url in route_payload:
                return Mock(**{'json.return_value': route_payload[url]})
            return HTTPError

        cls.get_patcher = patch("requests.get", side_effect=get_payload)
        cls.get_patcher.start()

    @classmethod
    def tearDownClass(cls) -> None:
        """Tear Down"""
        cls.get_patcher.stop()

    def test_public_repos(self):
        """
        Test that `GithubOrgClient.public_repos` returns the correct value.
        """
        self.assertEqual(
            GithubOrgClient("google").public_repos(),
            self.expected_repos,
        )

    def test_public_repos_with_license(self):
        """
        Test that `GithubOrgClient.public_repos`
        returns the correct value given a license.
        """
        self.assertEqual(
            GithubOrgClient("google").public_repos(license="apache-2.0"),
            self.apache2_repos,
        )
