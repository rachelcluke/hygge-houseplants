from django.test import TestCase


class TestViews(TestCase):
    """ Test Views in Bag App """

    def test_get_bag_page(self):
        """ Test bag.html view """
        response = self.client.get('/bag/')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'bag/bag.html')
