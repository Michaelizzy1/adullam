from django.shortcuts import render
from .models import Sites, Graphic

# Create your views here.


def index(request):
    sites = Sites.objects.all()
    images = Graphic.objects.all()
    context = {
        'sites':sites,
        'images':images,
    }
    return render(request, 'portfolio/index.html', context)