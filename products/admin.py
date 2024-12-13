from django.contrib import admin
from .models import Category, Care, Light, Product, Discount
from django.contrib import admin
from .models import Product, Category

class ProductAdmin(admin.ModelAdmin):
    list_display = (
        'category_ref',
        'product_name',
        'species',
        'product_description',
        'price',
        'rating',
        'image',
        'care_ref',
        'light_ref',
        'pet_friendly'
    )

class CategoryAdmin(admin.ModelAdmin):
    list_display = (
        'user_friendly_name',
        'name',
    )

admin.site.register(Product, ProductAdmin)
admin.site.register(Category, CategoryAdmin)
admin.site.register(Care)
admin.site.register(Light)
admin.site.register(Discount)