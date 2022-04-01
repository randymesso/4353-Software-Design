from .models import UserCredentials, ClientInformation   
    
from django.test import TestCase

class UsersManagersTests(TestCase):

    def test_create_user(self):
        user = UserCredentials.objects.create_user(username='Test_Guy', password='foo')
        self.assertEqual(user.username, 'Test_Guy')
        self.assertTrue(user.is_active)
        self.assertFalse(user.is_staff)
        self.assertFalse(user.is_superuser)
        try:
            self.assertEqual(user.username, 'Test_Guy')
        except AttributeError:
            pass
        with self.assertRaises(TypeError):
            UserCredentials.objects.create_user()
        with self.assertRaises(TypeError):
            UserCredentials.objects.create_user(username='')
        with self.assertRaises(ValueError):
            UserCredentials.objects.create_user(username='', password="foo")

"""
class ProfileManagerTest(TestCase):
    def test_profile_create(self):
        
"""