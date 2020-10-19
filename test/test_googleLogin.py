import mock

import google.auth.credentials
import google_auth_httplib2
import httplib2
import oauth2client.client
import unittest2 as unittest

from googleapiclient import _auth


class TestAuthWithGoogleAuth(unittest.TestCase):
    def setUp(self):
        _auth.HAS_GOOGLE_AUTH = True
        _auth.HAS_OAUTH2CLIENT = False

    def tearDown(self):
        _auth.HAS_GOOGLE_AUTH = True
        _auth.HAS_OAUTH2CLIENT = True

    def test_credentials_from_file(self):
        with mock.patch(
            "google.auth.load_credentials_from_file", autospec=True
        ) as default:
            default.return_value = (mock.sentinel.credentials, mock.sentinel.project)

            credentials = _auth.credentials_from_file("credentials.json")

            self.assertEqual(credentials, mock.sentinel.credentials)
            default.assert_called_once_with(
                "credentials.json", scopes=None, quota_project_id=None
            )