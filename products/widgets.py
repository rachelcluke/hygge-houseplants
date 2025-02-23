# Source: https://github.com/django/django/blob/main/django/forms/templates/django/forms/widgets/clearable_file_input.html

from django.forms.widgets import ClearableFileInput
from django.utils.translation import gettext_lazy as _


class CustomClearableFileInput(ClearableFileInput):
    """Widget Class for Admin to input/remove product image"""
    clear_checkbox_label = _('Remove')
    initial_text = _('Current Image')
    input_text = _('')
    template_name = 'products/custom_widget_templates/custom_clearable_file_input.html'