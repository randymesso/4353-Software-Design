from django.contrib.auth import get_user_model
from django.test import TestCase

class UsersManagersTests(TestCase):

    def test_create_user(self):
        User = get_user_model()
        user = User.objects.create_user(username='Test_Guy', password='foo')
        self.assertEqual(user.username, 'Test_Guy')
        self.assertTrue(user.is_active)
        self.assertFalse(user.is_staff)
        self.assertFalse(user.is_superuser)
        try:
            self.assertEqual(user.username, 'Test_Guy')
        except AttributeError:
            pass
        with self.assertRaises(TypeError):
            User.objects.create_user()
        with self.assertRaises(TypeError):
            User.objects.create_user(username='')
        with self.assertRaises(ValueError):
            User.objects.create_user(username='', password="foo")

    def test_create_superuser(self):
        User = get_user_model()
        admin_user = User.objects.create_superuser(username='Super_Test_Guy', password='foo')
        self.assertEqual(admin_user.username, 'Super_Test_Guy')
        self.assertTrue(admin_user.is_active)
        self.assertTrue(admin_user.is_staff)
        self.assertTrue(admin_user.is_superuser)
        try:
            self.assertEqual(admin_user.username,'Super_Test_Guy')
        except AttributeError:
            pass
        with self.assertRaises(ValueError):
            User.objects.create_superuser(
                username='Super_Test_Guy', password='foo', is_superuser=False)