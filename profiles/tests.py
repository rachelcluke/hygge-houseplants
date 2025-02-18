from django.test import TestCase
from django.contrib.auth.models import User


class TestViews(TestCase):
    """ Test Views in Profiles App """

    def setUp(self):
        """ Create a user """
        self.user = User.objects.create_user(
            username="myUsername", password="myPassword", email="test@test.com")

    def test_get_profile_page(self):
        """ Test profile.html view """
        self.client.login(username="myUsername", password="myPassword")
        response = self.client.get('/profile/')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response,'profiles/profile.html')
