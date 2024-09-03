from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from .models import Car, Cleaning
from .forms import CleaningForm
from django.urls import reverse
from django.contrib.auth.views import LoginView
from django.views.generic import ListView, DetailView
from django.contrib.auth import login
from django.contrib.auth.forms import UserCreationForm


class Home(LoginView):
    template_name = 'home.html'

def about(request):
    return render(request, 'about.html')

def car_index(request):
    cars = Car.objects.filter(user=request.user)
    return render(request, 'cars/index.html', {'cars': cars})

def car_detail(request, car_id):
    car = Car.objects.get(id=car_id)
    return render(request, 'cars/details.html', {'car': car})

class CarCreate(CreateView):
    model = Car
    fields = '__all__'
    success_url = '/cars/'
    def form_valid(self, form):
        form.instance.user = self.request.user  
        return super().form_valid(form)

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

def signup(request):
    error_message = ''
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('car-index')
        else:
            error_message = 'Invalid sign up - try again'
    form = UserCreationForm()
    context = {'form': form, 'error_message': error_message}
    return render(request, 'signup.html', context)
   