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
