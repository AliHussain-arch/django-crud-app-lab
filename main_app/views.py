from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from .models import Car

def home(request):
    return HttpResponse('<h1>Hello You are on the landing page!</h1>')

def about(request):
    return render(request, 'about.html')

def car_index(request):
    cars = Car.objects.all()
    return render(request, 'cars/index.html', {'cars': cars})

def car_detail(request, car_id):
    car = Car.objects.get(id=car_id)
    return render(request, 'cars/details.html', {'car': car})

class CarCreate(CreateView):
    model = Car
    fields = ['make', 'model', 'description', 'year']

class CarCreate(CreateView):
    model = Car
    fields = '__all__'
    success_url = '/cars/'

class CarUpdate(UpdateView):
    model = Car
    fields = ['make', 'model', 'description', 'year']

class CarDelete(DeleteView):
    model = Car
    success_url = '/cars/'