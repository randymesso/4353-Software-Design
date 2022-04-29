from .models import UserCredentials, ClientInformation, Fuel_Quote
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

class ProfileManagerTest(TestCase):
    def test_profile_create(self):
        user = UserCredentials.objects.create_user(username='Profile_Test_Guy', password='foo')
        profile = user.clientinformation
        
        profile.fullname = "Test G User"
        
        try:
            self.assertEqual(user.username, 'Profile_Test_Guy')
        except AttributeError:
            pass
            
class FuelQuoteTest(TestCase):
    def test_create_quote(self):
        user = UserCredentials.objects.create_user(username='Profile_Test_Guy', password='foo')
        profile = user.clientinformation
        profile.address1 = "8394 Super Lane"
        profile.state = "TX"
        profile.city = "Austin"
        
        try: 
            purchase = Fuel_Quote.objects.create(gallons_requested = 10,delivery_address=profile.address1+profile.state+profile.city)
        except AttributeError:
            pass
        