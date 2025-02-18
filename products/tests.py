from django.test import TestCase
from django.contrib.auth.models import User
from django.test.client import Client
from .forms import ProductForm
from .models import Product

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

    # TODO - resolve
    def test_get_add_product_page(self):
        """ Test add_product.html view """
        # superadmin credentials
        self.client = Client()
        self.user = User.objects.create_user('john', 'lennon@thebeatles.com', 'johnpassword122!')
        self.client.login(username='john', password='johnpassword122!')
        # end of superadmin
        response = self.client.get('/products/add/')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'products/add_product.html')

    # TODO - resolve
    def test_get_edit_product_page(self):
        """ Test edit_product.html view """
        # superadmin credentials
        password = 'mypassword1223!!' 
        my_admin = User.objects.create_superuser('myemail@test.com', 'myuser1', password)
        c = Client()
        c.login(username=my_admin.username, password=password)
        # end of superadmin
        product = Product.objects.create(product_name='Test Product', product_description='x', price='2.00')
        response = self.client.get(f'/products/edit/{product.id}')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'products/edit_product.html')

    # TODO - resolve 
    def test_get_delete_product_page(self):
        """ Test delete_product goes back to home view """
        # superadmin credentials
        password = 'mypassword1223!!' 
        my_admin = User.objects.create_superuser('myemail@test.com', 'myuser1', password)
        c = Client()
        c.login(username=my_admin.username, password=password)
        # end of superadmin
        product = Product.objects.create(product_name='Test Product', product_description='x', price='2.00')
        response = self.client.get(f'/products/delete/{product.id}')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, '/')
        existing_products = Product.objects.filter(id=product.id)
        self.assertEqual(len(existing_products), 0)
