from django import template


register = template.Library()

@register.filter(name='calc_subtotal')
def calc_subtotal(price, quantity):
    """ Calculate subtotal by multiplying price and quantity """

    return price * quantity