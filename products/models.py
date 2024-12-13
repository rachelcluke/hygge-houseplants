from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator

class Category(models.Model):
    """Category Class contains category name and category user friendly name."""
    class Meta:
        verbose_name_plural = 'Categories'
        
    name = models.CharField(max_length=254)
    user_friendly_name = models.CharField(max_length=254, null=True, blank=True)

    def __str__(self):
        """Method to return Cateogry name."""
        return self.name

    def get_user_friendly_name(self):
        """Method to return Category user friendly name."""
        return self.user_friendly_name

class Care(models.Model):
    """Plant Level of Care Class contains care name and care user friendly name."""
    care_name = models.CharField(max_length=20)
    care_friendly_name = models.CharField(max_length=254, null=True, blank=True)

    def __str__(self):
        """Method to return Care name."""
        return self.care_name

    def get_care_friendly_name(self):
        """Method to return Care user friendly name."""
        return self.care_friendly_name

class Light(models.Model):
    """Plant Level of Light Class contains light name and light user friendly name."""
    light_name = models.CharField(max_length=20)
    light_friendly_name = models.CharField(max_length=254, null=True, blank=True)

    def __str__(self):
        """Method to return Light name."""
        return self.light_name

    def get_light_friendly_name(self):
        """Method to return Light user friendly name."""
        return self.light_friendly_name

class Product(models.Model):
    """Products Class has relationship with Category db, Care db, Light db and contains name, species, description, sale?, price, sale price, category, rating, image, image_url, level of care, level of light, and pet-friendly?."""
    category_ref = models.ForeignKey('Category', null=True, blank=True, on_delete=models.CASCADE)
    product_name = models.CharField(max_length=100)
    species = models.CharField(max_length=200, blank=True)
    product_description = models.TextField()
    sale = models.BooleanField(default=False, null=True, blank=True)
    price = models.DecimalField(max_digits=6, decimal_places=2)
    sale_price = models.DecimalField(max_digits=6, decimal_places=2, blank=True)
    rating = models.DecimalField(max_digits=6, decimal_places=2, null=True, blank=True)
    image_url = models.URLField(max_length=1020, null=True, blank=True)
    image = models.ImageField(null=True, blank=True)
    care_ref = models.ForeignKey('Care', null=True, blank=True, on_delete=models.CASCADE)
    light_ref = models.ForeignKey('Light', null=True, blank=True, on_delete=models.CASCADE)
    pet_friendly = models.BooleanField(default=False, null=True, blank=True)

    def __str__(self):
        """Magic Method to return Products category, name, species, description, sale?, price, sale_price, rating, image_url, image, care, light, pet_friendly."""
        return self.category_ref, self.product_name, self.species, self.product_description, self.sale, self.price, self.sale_price, self.rating, self.image_url, self.image, self.care_ref, self.light_ref, self.pet_friendly

class Discount(models.Model):
    """Discount Class contains code, discount, active?, validity_start and validity_end."""
    code = models.CharField(max_length=50)
    discount = models.IntegerField(blank=True, default=0,
        validators=[MaxValueValidator(99), MinValueValidator(1)])
    discount_description = models.TextField()
    active = models.BooleanField(default=False, null=True, blank=True)
    validity_start = models.DateTimeField()
    validity_end = models.DateTimeField()

    @property
    def discount_in_percentage(self):
        """Method to convert discount field to percentage format."""
        return f"{self.discount} %"

    def __str__(self):
        """Magic Method to return Discount code, discount %, active?, validity_start, validiy end."""
        return self.code, self.discount, self.discount_description, self.active, self.validity_start, self.validity_end