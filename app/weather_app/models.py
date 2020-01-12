from django.db import models
from django import forms
from django.contrib.postgres.fields import JSONField



class Cities(models.Model):
    id = models.BigAutoField(primary_key=True)
    name = models.TextField(max_length=256, unique=True)
    latitude_deg = models.DecimalField(max_digits=50, decimal_places=15)
    longitude_deg = models.DecimalField(max_digits=50, decimal_places=15)
    country = models.TextField(max_length=256)

class WeatherArchive(models.Model):
    id = models.BigAutoField(primary_key=True)
    last_update_timestamp = models.DateTimeField()
    city = models.ForeignKey(Cities, to_field='name', on_delete=models.CASCADE)
    weather = JSONField()
