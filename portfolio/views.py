from django.shortcuts import render
from .models import Sites, Graphic, Defaultpic

# Create your views here.


def index(request):
    sites = Sites.objects.all()
    images = Graphic.objects.all()
    img = Defaultpic.objects.all()
    context = {
        'sites':sites,
        'images':images,
        'img': img,
    }
    return render(request, 'portfolio/index.html', context)


def about(request):
    img = Defaultpic.objects.all()
    context = {
        'img':img
    }
    return render(request, 'portfolio/about.html', context)


def contact(request):
    return render(request, 'portfolio/contact.html')


def sites(request):
    sites = Sites.objects.all()
    context = {
        'sites':sites
    }
    return render(request, 'portfolio/sites.html', context)