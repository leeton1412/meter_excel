from django.shortcuts import render
from .models import Meters

# Create your views here.


def index(request):
    return render(request, 'index.html')


def data(request):
    items = Meters.objects.all()
    context = {
        'items': items,
    }
    
    return render(request, 'index.html', context)
