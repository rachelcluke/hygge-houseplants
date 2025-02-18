from django.test import TestCase
from .models import Product

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
