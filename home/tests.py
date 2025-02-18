from django.test import TestCase

class TestViews(TestCase):
    """ Test Views in Products App """

    def test_get_home_page(self):
        """ Test index.html view """
        response = self.client.get('/')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response,'home/index.html')