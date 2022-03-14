from django.test import TestCase
from backend.models import Profile

class ProfileTestCase(TestCase):
    def setUp(self):
        Profile.objects.create()
