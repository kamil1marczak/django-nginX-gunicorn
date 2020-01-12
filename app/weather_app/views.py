from django.views import View
from django.shortcuts import render
from weather_app.weather_api import WeatherApi
from weather_app.utils import date_time_now
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from weather_app.models import Cities, WeatherArchive
# from weather_app.flights_archive import FlightArchive
from django.core.paginator import Paginator
from weather_app.views_authentication import SuperUserCheck
from weather_app.weather_archive import WeatherArchiveCreator
from django.utils import timezone

# Create your views here.


class IndexView(View):
    def get(self, request):
        return render(request, 'index.html')

class WeatherData(View):
    @method_decorator(login_required)
    def get(self, request, lat, lon):
        weather_data_context = WeatherApi.weather_json_restructure(lat, lon)

        return render(request, 'rendered_tables/weather_data.html',
                      context=weather_data_context)

class CityWeatherMain(View):
    @method_decorator(login_required)
    def get(self, request):
        cities_data = Cities.objects.all()
        return render(request, 'show_cities.html', context={
            'cities_data':cities_data,
        })

class CityWeatherRender(View):
    @method_decorator(login_required)
    def get(self, request, name):
        weather_data_context = WeatherApi.city_name_weather(name)

        return render(request, 'rendered_tables/weather_data.html',
                      context=weather_data_context)



class SaveToWeatherArchiveView(SuperUserCheck, View):
    def get(self, request):
        cities_data = Cities.objects.all()

        return render(request, 'weather_archive/save_weather_archive.html', context={'cities_data': cities_data})

    def post(self, request):

        city_selector = request.POST.get('city_list')

        WeatherArchiveCreator.save_to_weather_archive(city_selector)

        return render(request, 'weather_archive/save_weather_archive.html',
                      context={'city_selector': city_selector})



class ViewWeatherArchive(View):
    @method_decorator(login_required)
    def get(self, request):

        paginator_selector = request.GET.get('paginator-selector')
        weather_archive_serch = request.GET.get('weather-archive-serch')

        if weather_archive_serch:
            weather_all = WeatherArchiveCreator.render_weather_archive(weather_archive_serch)
        else:
            weather_all = WeatherArchiveCreator.render_weather_archive(None)

        if paginator_selector == None:
            paginator_selector = 25
        paginator = Paginator(weather_all, int(paginator_selector))
        page = request.GET.get('page')
        weather_all_paginator = paginator.get_page(page)

        return render(request, 'weather_archive/weather_archive_dashboard.html', context={
            'weather_all': weather_all_paginator, 'weather_archive_serch': weather_archive_serch
        })

