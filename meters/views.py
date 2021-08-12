from django.shortcuts import render
from django.http import HttpResponse
from .models import Meters
from .forms import contactForm

# Create your views here.


def index(request):
    return render(request, 'index.html')


def data(request):
    items = Meters.objects.all()
    form = contactForm()
    print(contactForm)
    print(form)
    context = {
        'items': items,
        'contactForm': form,
    }
    
    return render(request, 'index.html', context)

