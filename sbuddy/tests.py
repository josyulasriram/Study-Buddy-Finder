import datetime

import mock

import google.auth.credentials
import google_auth_httplib2
import httplib2
import oauth2client.client
import unittest2 as unittest

from django.test import TestCase
from django.utils import timezone
from sbuddy.models import User
import sbuddy.views as views



from googleapiclient import _auth


class UserModelTests(TestCase):

    def test_match_strengths(self):
        person = User()
        person.strengths = "English, Communication"

        person2 = User()
        person2.strengths = "English, Computer Science"

        self.assertIs(views.do_items_match(person.strengths[0], person2.strengths[0]), True)

    def test_no_match_strengths(self):
        person = User()
        person.strengths = "English, Communication"

        person2 = User()
        person2.strengths = "Mathematics, Computer Science"

        self.assertIs(views.do_items_match(person.strengths[0], person2.strengths[0]), False)


    def test_no_match_skills(self):
        person = User()
        person.skills = "English, Writing"

        person2 = User()
        person2.skills = "Reading, Communication"

        self.assertIs(views.do_items_match(person.skills[0], person2.skills[0]), False)

    def test_match_skills(self):
        person = User()
        person.skills = "English, Writing, Mathematics"

        person2 = User()
        person2.skills = "Reading, Communication, English"

        self.assertIs(views.do_items_match(person.skills[0], person2.skills[2]), False)
        
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

