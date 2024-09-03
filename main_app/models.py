from django.db import models
from django.urls import reverse

class Car(models.Model):
    make = models.CharField(max_length=100)
    model = models.CharField(max_length=100)
    description = models.TextField(max_length=250)
    year = models.IntegerField()

    def __str__(self):
        return f"{self.make} {self.model}"

    def get_absolute_url(self):
        return reverse('car-detail', kwargs={'car_id': self.id})
    

