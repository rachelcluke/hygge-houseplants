from django.shortcuts import render, redirect, reverse
from django.contrib import messages
from .forms import OrderForm


def checkout(request):
    bag = request.session.get('bag', {})
    if not bag:
        messages.error(request, "Your bag is currently empty.")
        return redirect(reverse('products'))

    order_form = OrderForm()
    template = 'checkout/checkout.html'
    context = {
        'order_form': order_form,
        'stripe_public_key': 'pk_test_51QpUDDF9uUBrkCnyx8qam52fOQ5sM2pfY50rlQ7kg8DgJNJao0zZoc0JGoiS9tXYBWhwgPsFJXiY666tOQmwqEb300QJLN6P6c',
        'client_secret': 'test client secret',
    }

    return render(request, template, context)

