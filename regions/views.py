from django.shortcuts import render, redirect
from .models import *


def home(request):
    context = {
        'country': Country.objects.order_by('id')[::-1]
    }

    return render(request, 'home.html', context)


def asia(request):
    continent = Continent.objects.get(id=1)
    context = {'country': continent.country_set.all()}

    return render(request, 'asia.html', context)


def europe(request):
    continent = Continent.objects.get(id=2)
    context = {
        'country': continent.country_set.all()
    }

    return render(request, 'europe.html', context)


def north_america(request):
    continent = Continent.objects.get(id=4)
    context = {
        'country': continent.country_set.all()
    }

    return render(request, 'north-america.html', context)


def south_america(request):
    continent = Continent.objects.get(id=5)
    context = {
        'country': continent.country_set.all()
    }

    return render(request, 'south-america.html', context)


def africa(request):
    continent = Continent.objects.get(id=3)
    context = {
        'country': continent.country_set.all()
    }

    return render(request, 'africa.html', context)


def oceania(request):
    continent = Continent.objects.get(id=6)
    context = {
        'country': continent.country_set.all()
    }

    return render(request, 'oceania.html', context)


def create(request):
    if request.method == 'POST':
        c = Country(name=request.POST['name'], capital=request.POST['capital'],
                    language=request.POST['language'], population=request.POST['population'], area=request.POST['area'])
        c.save()
        return redirect('home')
    return render(request, 'create.html')


def delete(request, pk):
    Country.objects.filter(id=pk).delete()
    return redirect('home')


def update(request, pk):
    try:
        c = Country.objects.get(id=pk)
    except Country.DoesNotExist:
        return redirect('home')
    if request.method == 'POST':
        c.name = request.POST["name"]
        c.capital = request.POST["capital"]
        c.language = request.POST["language"]
        c.population = request.POST["population"]
        c.capital = request.POST["area"]
        c.save()
        return redirect("home")
    return render(request, 'create.html', {'c': c})
