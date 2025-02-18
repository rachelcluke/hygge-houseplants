from django.test import TestCase
from django.contrib.auth.models import User
from django.test.client import Client
from .forms import UserProfileForm

"""
class LoginTestCase(TestCase):
    def setUp(self):
        self.client = Client()
        self.user = User.objects.create_user('wedn01', 'pear@prg.com', 'jKs9bN!8j38')

    def testLogin(self):
        self.client.login(username='wedn01', password='jKs9bN!8j38')
        response = self.client.get(reversed('login'))
        self.assertEqual(response.status_code, 200)
"""

# TODO - resolve
class TestViews(TestCase):
    """ Test Views in Profiles App """

    def test_get_profile_page(self):
        """ Test profile.html view """
        response = self.client.get('/profile/')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response,'profiles/profile.html')
