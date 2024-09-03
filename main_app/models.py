from django.db import models
from django.urls import reverse
from django.contrib.auth.models import User

class Car(models.Model):
    make = models.CharField(max_length=100)
    model = models.CharField(max_length=100)
    description = models.TextField(max_length=250)
    year = models.IntegerField()
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.make} {self.model}"

    def get_absolute_url(self):
        return reverse('car-detail', kwargs={'car_id': self.id})

TIME = (
    ('M', 'Morning'),
    ('A', 'Afternoon'),
    ('E', 'Evening')
)

class Cleaning(models.Model):
    date = models.DateField()
    time = models.CharField(max_length=1, choices=TIME, default=TIME[0][0] )

    car = models.ForeignKey(Car, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.get_time_display()} on {self.date}"

    class Meta:
        ordering = ['-date'] 

