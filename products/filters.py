import django_filters

from .models import Product


class ProductFilter(django_filters.FilterSet):
    """Filter plant products based on their care level, 
    light level and if they are pet friendly."""

    care_ref_low = Product.objects.filter(light_ref=[0]).values()
    care_ref_medium = Product.objects.filter(light_ref=[1]).values()
    care_ref_high = Product.objects.filter(light_ref=[2]).values()

    light_ref_low = Product.objects.filter(light_ref=[0]).values()
    light_ref_medium = Product.objects.filter(light_ref=[1]).values()
    light_ref_high = Product.objects.filter(light_ref=[2]).values()

    pet_friendly_true = Product.objects.filter(pet_friendly="True").values()

    class Meta:
        model = Product
        fields = ['care_ref', 'light_ref', 'pet_friendly']
    
    def product_filter(self, queryset, name, value):
        """Function to return filtered product queries """
        return queryset.filter(**{
            name: value,
        })
