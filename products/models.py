from django.db import models

class Category(models.Model):
    """Category Class contains category name and category user friendly name."""
    name = models.CharField(max_length=50)
    user_friendly_name = models.CharField(max_length=50, null=True, blank=True)

    def __str__(self):
        return self.name

    def get_user_friendly_name(self):
        return self.user_friendly_name


class Product(models.Model):
    """Products Class has relationship with Category db and contains sku, name, description, price, rating, image_url and image."""

    category = models.ForeignKey('Category', null=True, blank=True, on_delete=models.SET_NULL)
    sku = models.CharField(max_length=100, null=True, blank=True)
    name = models.CharField(max_length=50)
    description = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    rating = models.DecimalField(max_digits=6, decimal_places=2, null=True, blank=True)
    image = models.ImageField(null=True, blank=True)
    image_url = models.URLField(max_length=1000, null=True, blank=True)

    def __str__(self):
        return self.name