from django.test import TestCase
from .forms import OrderForm

class TestOrderForm(TestCase):
    """ Test Order Form in Checkout App """

    def test_order_form_fields_are_required(self):
        """ Test form instance is valid """
        form = OrderForm({'full_name': '', 'email': '', 'phone_number':'', 'street_address1': '', 'town_or_city': ''})
        self.assertFalse(form.is_valid())
        self.assertIn('full_name', form.errors.keys())
        self.assertEqual(form.errors['full_name'][0], 'This field is required.')
    
    def test_fields_are_explicit_in_form_metaclass(self):
        """ Test form instance meta fields """
        form = OrderForm()
        self.assertEqual(form.Meta.fields, ('full_name', 'email', 'phone_number',
                  'street_address1', 'street_address2',
                  'town_or_city', 'postcode', 'country',
                  'county'))

class TestViews(TestCase):
    """ Test Views in Checkout App """

    # TODO - resolve
    def test_get_checkout_page(self):
        """ Test checkout.html view """
        response = self.client.get('/checkout/')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response,'checkout/checkout.html')
