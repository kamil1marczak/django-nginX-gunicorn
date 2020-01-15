from django.views import View
from django.shortcuts import render

import json
from datetime import datetime, timedelta
from weather_app.weather_api import WeatherApi
from weather_app.models import WeatherArchive, Cities
from django.contrib.auth.models import User


class WeatherArchiveCreator:
    @staticmethod
    def save_to_weather_archive(city, username):
        cities_data = Cities.objects.get(name=city)
        lat = cities_data.latitude_deg
        lon = cities_data.longitude_deg
        weather = WeatherApi.connect_to_api(lat, lon)
        user = User.objects.get(username=username)
        WeatherArchive.objects.create(last_update_timestamp=datetime.now() + timedelta(hours=1), city=cities_data, weather=weather, user=user)

    @staticmethod
    def render_weather_archive(serch, username):
        user = User.objects.get(username=username)
        if serch == None:
            weather_all = WeatherArchive.objects.filter(user=user)
        else:
            weather_all = WeatherArchive.objects.filter(city=serch, user=user)

        return weather_all





