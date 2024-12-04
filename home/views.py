from django.shortcuts import render
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
from django.views.decorators.csrf import csrf_protect

def index(request):
    """ A view to return the index page """

    return render(request, 'home/index.html')

from django.shortcuts import render