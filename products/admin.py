from django.contrib import admin
from .models import Category, Care, Light, Product, Discount


class ProductAdmin(admin.ModelAdmin):
    """ Product Admin Model to set list display"""
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
    """ Category Admin Model to set list display """
    list_display = (
        'user_friendly_name',
        'name',
    )


admin.site.register(Product, ProductAdmin)
admin.site.register(Category, CategoryAdmin)
admin.site.register(Care)
admin.site.register(Light)
admin.site.register(Discount)
