from django.shortcuts import render, redirect, reverse, get_object_or_404
from django.contrib import messages
from django.db.models import Q
from .models import Product, Category

def all_products(request):
    """ A view to show all products, including sort and search queries """

    products = Product.objects.all()
    query = None
    categories = None


    if request.GET:
        if 'category' in request.GET:
            categories = request.GET['category'].split(',')
            products = products.filter(category_ref__name__in=categories)
            categories = Category.objects.filter(name__in=categories)

        if 'q' in request.GET:
            query = request.GET['q']
            if not query:
                messages.error(request, "Search criteria is empty.")
                return redirect(reverse('products'))
            
            queries = Q(product_name__icontains=query) | Q(product_description__icontains=query)
            products = products.filter(queries)

    context = {
        'products': products,
        'search_term': query,
        'current_categories': categories,
    }

    return render(request, 'products/products.html', context)

def product_info(request, product_id):
    """ A view to show individual product details """

    product = get_object_or_404(Product, pk=product_id)
    context = {'product': product}

    return render(request, 'products/product_info.html', context)
