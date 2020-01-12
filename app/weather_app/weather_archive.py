from django.views import View
from django.shortcuts import render

import json
from datetime import datetime, timedelta
from weather_app.weather_api import WeatherApi
from weather_app.models import WeatherArchive, Cities


class WeatherArchiveCreator:
    @staticmethod
    def save_to_weather_archive(name):
        weather = WeatherApi.city_name_weather(name)
        WeatherArchive.objects.create(last_update_timestamp=datetime.now() + timedelta(hours=1), city=Cities.objects.get(name=name), weather=weather)

    @staticmethod
    def render_weather_archive(serch):
        if serch == None:
            weather_all = WeatherArchive.objects.all()
        else:
            weather_all = WeatherArchive.objects.filter(city=serch)

        return weather_all





