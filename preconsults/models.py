from django.db import models
from django.utils import timezone
from datetime import date

class Preconsult(models.Model):
    name = models.CharField(max_length=100)
    phone = models.CharField(max_length=40)
    age = models.CharField(max_length=3)
    profession = models.CharField(max_length=50)
    surgery = models.TextField(max_length=500)
    expectancy = models.TextField(max_length=1000)
    fear = models.TextField(max_length=1000)
    recommendation = models.TextField(max_length=100)
    rhinoplasty = models.BooleanField(default=False)
    checklink = models.BooleanField(default=False)
    active = models.BooleanField(default=True)
    creation_date = models.DateField(default=date.today)
    creation_time = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.name

