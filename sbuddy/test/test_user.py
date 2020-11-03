from django.test import TestCase
from .models import User

class UserTest(TestCase):
	def setUp(self):
		User.objects.create(name="Sriram",strengths = "Math",skills = "Java")

	def test_Users(self):
		user1 = User.objects.get(name="Sriram")
		assertEquals(user1.name, "Sriram")