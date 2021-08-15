from django.shortcuts import render
from django.http import HttpResponse
from .models import Meters
from .forms import highestDay, highestNight, highestTotal

# Create your views here.


def index(request):
    return render(request, 'index.html')


def data(request):
    items = Meters.objects.all()
    high_day = highestDay()
    high_night = highestNight()
    high_total = highestTotal()
    context = {
        'items': items,
        'high_day': high_day,
        'high_night': high_night,
        'high_total': high_total,
    }
    
    return render(request, 'index.html', context)

