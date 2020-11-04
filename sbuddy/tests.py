import datetime

from django.test import TestCase
from django.utils import timezone
from sbuddy.models import User
import sbuddy.views as views


class UserModelTests(TestCase):

    def test_match_strengths(self):
        personA = User("George", "Mathematics", "Reading, Writing", None, timezone.now())
        personB = User("Lily", "Mathematics", "English", None, timezone.now())

        self.assertIs(views.do_items_match(personA.strengths, personB.strengths), True)

    def test_no_match_strengths(self):
        personA = User("George", "English", "Reading, Writing", None, timezone.now())
        personB = User("Lily", "Mathematics", "English", None, timezone.now())

        self.assertIs(views.do_items_match(personA.strengths, personB.strengths), False)


    def test_no_match_skills(self):
        personA = User("George", "Mathematics", "Reading, Writing", None, timezone.now())
        personB = User("Lily", "Mathematics", "English", None, timezone.now())

        self.assertIs(views.do_items_match(personA.skills, personB.skills), False)

    def test_match_skills(self):
        personA = User("George", "Mathematics", "Reading, Writing", None, timezone.now())
        personB = User("Katie", "English", "Reading", None, timezone.now())

        self.assertIs(views.do_items_match(personA.skills, personB.skills), True)
