from django.test import TestCase
from django.contrib.auth.models import User
from .forms import UserProfileForm
from .models import UserProfile


class TestUserProfileForm(TestCase):
    """ Test Form in Profiles App """

    def test__name_is_required(self):
        """ Test UserProfile form """
        form = UserProfileForm({})
        self.assertFalse(form.is_valid())


class TestUserProfileViews(TestCase):
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

class TestUserProfileModels(TestCase):
    """ Test UserProfile Models in Profiles App """
    def test_user_profile_model(self):
        """ Test UserProfile model """
        newuser = User.objects.create_user(username="newUser", password="myPassword", email="test10@test.com")
        userprofile = UserProfile.objects.get(user_id=newuser.id)
        self.assertTrue(userprofile)
