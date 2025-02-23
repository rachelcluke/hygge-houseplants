from django import forms
from .widgets import CustomClearableFileInput
from .models import Product, Category


class ProductForm(forms.ModelForm):
    """ Products Model Form """
    class Meta:
        model = Product
        fields = '__all__'

    image = forms.ImageField(label='Image', required=False, 
                             widget=CustomClearableFileInput)

    def __init__(self, *args, **kwargs):
        """ Return category friendly names """
        super().__init__(*args, **kwargs)
        categories = Category.objects.all()
        user_friendly_names = [(c.id, c.get_user_friendly_name()) for c in categories]

        self.fields['category_ref'].choices = user_friendly_names
        for field_name, field in self.fields.items():
            field.widget.attrs['class'] = 'border-black rounded-0'
