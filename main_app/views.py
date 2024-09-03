from django.shortcuts import render
from django.http import HttpResponse
from .models import Car

def home(request):
    return HttpResponse('<h1>Hello from main_app!</h1>')

def about(request):
    return render(request, 'about.html')

def car_index(request):
    cars = Car.objects.all()
    return render(request, 'cars/index.html', {'cars': cars})

def car_detail(request, car_id):
    car = Car.objects.get(id=car_id)
    return render(request, 'cars/details.html', {'car': car})
