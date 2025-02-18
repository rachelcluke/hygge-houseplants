from django.test import TestCase
from django.contrib.auth.models import User
from django.test.client import Client
from .forms import ProductForm
from .models import Product, Category, Light, Care, Discount

class TestProductForm(TestCase):
    """ Test Form in Products App """

    def test_product_name_is_required(self):
        """ Test Product Form instance is valid """
        form = ProductForm({'product_name': ''})
        self.assertFalse(form.is_valid())
        self.assertIn('product_name', form.errors.keys())
        self.assertEqual(form.errors['product_name'][0], 'This field is required.')
    
    def test_fields_are_explicit_in_form_metaclass(self):
        """ Test Product Form instance meta fields """
        form = ProductForm()
        self.assertEqual(form.Meta.fields, '__all__')


class TestViews(TestCase):
    """ Test Views in Products App """

    def setUp(self):
        """ Create a superuser """
        self.user = User.objects.create_superuser(
            username="myUsername", password="myPassword", email="test@test.com")

    def test_get_products_page(self):
        """ Test products.html view """
        response = self.client.get('/products/')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response,'products/products.html')
    
    def test_get_products_info_page(self):
        """ Test product_info.html view """
        product = Product.objects.create(product_name='Test Product', product_description='x', price='2.00')
        response = self.client.get(f'/products/{product.id}')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'products/product_info.html')

    def test_get_add_product_page(self):
        """ Test add_product.html view """
        self.client.login(username="myUsername", password="myPassword")
        response = self.client.get('/products/add/')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'products/add_product.html')

    def test_get_edit_product_page(self):
        """ Test edit_product.html view """
        self.client.login(username="myUsername", password="myPassword")
        product = Product.objects.create(product_name='Test Product', product_description='x', price='2.00')
        response = self.client.get(f'/products/edit/{product.id}/')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'products/edit_product.html')


class TestModels(TestCase):
    """ Test Category, Product, Care, Light& Discount Models in Products App """
    def test_category_model(self):
        """ Test category model """
        category = Category.objects.create(name='Category Test')
        self.assertTrue(category)
    
    def test_product_model(self):
        """ Test product model """
        product = Product.objects.create(product_name='Product Test')
        self.assertTrue(product)






