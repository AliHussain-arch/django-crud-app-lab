from django.db import models

class Car(models.Model):
    make = models.CharField(max_length=100)
    model = models.CharField(max_length=100)
    description = models.TextField(max_length=250)
    year = models.IntegerField()

    def __str__(self):
        return f"{self.make} {self.model}"

