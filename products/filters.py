import django_filters

from .models import Product, Category, Light, Care, Discount


class ProductFilter(django_filters.FilterSet):
    """Filter plant products based on their care level, light level and if they are pet friendly."""

    care_ref_low = Product.objects.filter(light_ref="low_care")
    care_ref_medium = Product.objects.filter(light_ref="medium_care")
    care_ref_high = Product.objects.filter(light_ref="high_care")

    light_ref_low = Product.objects.filter(light_ref="low_light")
    light_ref_medium = Product.objects.filter(light_ref="medium_light")
    light_ref_high = Product.objects.filter(light_ref="high_light")

    pet_friendly_true = Product.objects.filter(pet_friendly="True")

    class Meta:
        model = Product
        fields = ['care_ref', 'light_ref', 'pet_friendly']
    
    def product_filter(self, queryset, name, value):
        return queryset.filter(**{
            name: value,
        })
        queries = Q(product_name__icontains=query) | Q(product_description__icontains=query)
        products = products.filter(queries)
    
        context = {
            'products': products,
            'search_term': query,
            'sale_products:': sale_products,
            'current_categories': categories,
            'current_sorting': current_sorting,
        }
        return render(request, 'products/products.html', context)