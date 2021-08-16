from django.shortcuts import render, redirect
from .models import *


def home(request):
    context = {
        'country': Country.objects.order_by('id')[::-1]
    }

    return render(request, 'home.html', context)


def asia(request):
    continent = Continent.objects.get(name='asia')
    context = {
       'asia': continent.country_set
    }

    return render(request, 'home.html', context)


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
