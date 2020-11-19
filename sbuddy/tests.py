import datetime



from django.test import TestCase
from django.utils import timezone
from sbuddy.models import User
import sbuddy.views as views



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
        
    