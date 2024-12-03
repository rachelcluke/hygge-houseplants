from django.shortcuts import render

def get_landing_page(request):
 return render(request, 'hygge-houseplants/landing-page.html')