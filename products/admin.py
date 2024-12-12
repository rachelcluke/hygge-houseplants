from django.contrib import admin
from .models import Category, Care, Light, Product, Discount

admin.site.register(Category)
admin.site.register(Product)
admin.site.register(Care)
admin.site.register(Light)
admin.site.register(Discount)