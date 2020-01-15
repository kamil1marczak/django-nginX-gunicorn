from django.db import models
from django import forms
from django.contrib.postgres.fields import JSONField
from django.contrib.auth.models import User



class Cities(models.Model):
    id = models.IntegerField(primary_key=True)
    name = models.TextField(max_length=256, unique=True)
    latitude_deg = models.DecimalField(max_digits=50, decimal_places=15)
    longitude_deg = models.DecimalField(max_digits=50, decimal_places=15)
    country = models.TextField(max_length=256)

class WeatherArchive(models.Model):
    id = models.BigAutoField(primary_key=True)
    last_update_timestamp = models.DateTimeField()
    city = models.ForeignKey(Cities, to_field='name', on_delete=models.CASCADE)
    weather = JSONField()
    user = models.ForeignKey(User, to_field='username', on_delete=models.CASCADE)

class ApiKeys(models.Model):
    id = models.BigAutoField(primary_key=True)
    api_key = models.IntegerField(default=0)
    user = models.ForeignKey(User, to_field='username', on_delete=models.CASCADE)
