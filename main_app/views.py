from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from .models import Car, Cleaning
from .forms import CleaningForm
from django.urls import reverse


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

def car_detail(request, car_id):
    car = Car.objects.get(id=car_id)
    cleaning_form = CleaningForm()
    return render(request, 'cars/details.html', {
        'car': car, 'cleaning_form': cleaning_form
    })

def add_cleaning(request, car_id):
    form = CleaningForm(request.POST)
    if form.is_valid():
        new_cleaning = form.save(commit=False)
        new_cleaning.car_id = car_id
        new_cleaning.save()
    return redirect('car-detail', car_id=car_id)

class CleaningUpdate(UpdateView):
    model = Cleaning
    fields = ['date', 'time']
    template_name = 'cleanings/update.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['car_id'] = self.object.car.id
        return context

    def get_success_url(self):
        return reverse('car-detail', args=[self.object.car.id])

class CleaningDelete(DeleteView):
    model = Cleaning
    template_name = 'cleanings/delete_confirm.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['car_id'] = self.object.car.id
        return context

    def get_success_url(self):
        return reverse('car-detail', args=[self.object.car.id])

    