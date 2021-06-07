from django.db import models
from django.utils import timezone
from datetime import date

class Preconsult(models.Model):
    name = models.CharField(max_length=100)
    phone = models.CharField(max_length=40)
    age = models.CharField(max_length=100)
    height = models.CharField(max_length=100)
    weight = models.CharField(max_length=100)
    profession = models.CharField(max_length=50)
    surgery = models.TextField(max_length=500)
    expectancy = models.TextField(max_length=1000)
    fear = models.TextField(max_length=1000)
    recommendation = models.TextField(max_length=500)
    rhinoplasty = models.BooleanField(default=False)
    checklink = models.BooleanField(default=False)
    active = models.BooleanField(default=True)
    creation_date = models.DateField(default=date.today)
    creation_time = models.DateTimeField(default=timezone.now)
    check_prosthesis = models.BooleanField(default=False)
    check_mastopexy = models.BooleanField(default=False)
    check_liposculpture = models.BooleanField(default=False)
    check_abdominoplasty = models.BooleanField(default=False)
    check_lifting = models.BooleanField(default=False)
    check_rinoplasty = models.BooleanField(default=False)
    check_otoplasty = models.BooleanField(default=False)
    check_nymphoplasty = models.BooleanField(default=False)
    date_operate = models.CharField(max_length=10)
    type_rinoplasty = models.CharField(max_length=15)

    def __str__(self):
        return self.name

