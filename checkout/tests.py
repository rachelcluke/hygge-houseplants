from django.test import TestCase
from django.contrib.auth.models import User
from .forms import OrderForm
from .models import Order, OrderLineItem, Product

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

    def setUp(self):
        """ Create a user """
        self.user = User.objects.create_user(
            username="myUsername", password="myPassword12!!!", email="test00@test.com")

    # TODO - resolve
    def test_get_checkout_page(self):
        """ Test checkout.html view """
        self.client.login(username="myUsername", password="myPassword12!!!")
        response = self.client.get('/checkout')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response,'checkout/checkout.html')
    
    # TODO - resolve
    def test_get_checkout_success_page(self):
        """ Test checkout_success.html view """
        # user = User.objects.create_user(username="testUsername", password="myPass@495867", email="tester1@test.com")
        self.client.login(username="myUsername", password="myPassword12!!!")
        order = Order.objects.create(order_number=000, full_name='Yasmin Oh', phone_number = 29248, country='United Kingdom', town_or_city='x', street_address1='x' )
        response = self.client.get(f'/checkout-success/{order.order_number}')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response,'checkout/checkout_success.html')

class TestCheckoutModels(TestCase):
    """ Test Models in Checkout App """
    def test_order_model(self):
        """ Test Order model """
        testorder = Order.objects.create(order_number=000, full_name='Yasmin Oh', phone_number = 29248, country='United Kingdom', town_or_city='x', street_address1='x' )
        self.assertTrue(testorder)
    
    def test_order_line_model(self):
        """ Test Order Line Items model """
        testOrder = Order.objects.create(order_number=000, full_name='Yasmin Oh', phone_number = 29248, country='United Kingdom', town_or_city='x', street_address1='x' )
        testProduct = Product.objects.create(product_name='Test Product', product_description='x', price='2.00')
        test_orderLineItem = OrderLineItem.objects.create(order=testOrder, product=testProduct, quantity=1)
        self.assertTrue(test_orderLineItem)
