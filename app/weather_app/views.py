from django.views import View
from django.shortcuts import render
from weather_app.weather_api import WeatherApi

from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from weather_app.models import Cities, WeatherArchive, ApiKeys
# from weather_app.flights_archive import FlightArchive
from django.core.paginator import Paginator
from weather_app.views_authentication import SuperUserCheck
from weather_app.weather_archive import WeatherArchiveCreator
from django.utils import timezone
from rest_framework import viewsets
from weather_app.serializers import CitiesSerializer, WeatherArchiveSerializer, WeatherSerializer
from rest_framework.views import APIView
from django.http import Http404
from rest_framework.response import Response
from rest_framework import status
from datetime import datetime, timedelta


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

    @method_decorator(login_required)
    def post(self, request):
        city_selector = request.POST.get('city_list')
        username = request.user.username
        WeatherArchiveCreator.save_to_weather_archive(city_selector, username)

        cities_data = Cities.objects.all()
        return render(request, 'show_cities.html', context={
            'cities_data': cities_data,
        })


class CityWeatherRender(View):
    def city_name_weather(self, name):
        cities_data = Cities.objects.get(name=name)
        lat = cities_data.latitude_deg
        lon = cities_data.longitude_deg
        weather_data_context = WeatherApi.weather_json_restructure(lat, lon)
        return weather_data_context

    @method_decorator(login_required)
    def get(self, request, name):

        weather_data_context = self.city_name_weather(name)

        return render(request, 'rendered_tables/weather_data.html',
                      context=weather_data_context)


class SaveToWeatherArchiveView(View):
    def get(self, request):

        cities_data = Cities.objects.all()

        return render(request, 'weather_archive/save_weather_archive.html', context={'cities_data': cities_data})

    def post(self, request):

        city_selector = request.POST.get('city_list')
        username = request.user.username
        WeatherArchiveCreator.save_to_weather_archive(city_selector, username)

        return render(request, 'weather_archive/save_weather_archive.html',
                      context={'city_selector': city_selector})



class ViewWeatherArchive(View):
    @method_decorator(login_required)
    def get(self, request):
        username = request.user.username
        paginator_selector = request.GET.get('paginator-selector')
        weather_archive_serch = request.GET.get('weather-archive-serch')

        if weather_archive_serch:
            weather_all = WeatherArchiveCreator.render_weather_archive(weather_archive_serch, username)
        else:
            weather_all = WeatherArchiveCreator.render_weather_archive(None, username)

        if paginator_selector == None:
            paginator_selector = 25
        paginator = Paginator(weather_all, int(paginator_selector))
        page = request.GET.get('page')
        weather_all_paginator = paginator.get_page(page)

        return render(request, 'weather_archive/weather_archive_dashboard.html', context={
            'weather_all': weather_all_paginator, 'weather_archive_serch': weather_archive_serch
        })


class CitiesView(APIView):
    def get_object(self, city_name):
        try:
            return Cities.objects.get(name=city_name)
        except Cities.DoesNotExist:
            raise Http404
    def get(self, request, city_name, format=None):
        city = self.get_object(city_name)
        serializer = CitiesSerializer(city, context={"request": request})
        return Response(serializer.data)
    def delete(self, request, city_name, format=None):
        city = self.get_object(id)
        city.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

class WeatherArchiveView(APIView):
    def get_object(self, api_key):
        try:
            weather_list = []
            user = ApiKeys.objects.get(api_key=api_key).user
            for row in WeatherArchive.objects.filter(user=user):
                weather_list.append(row)
            return weather_list
        except Cities.DoesNotExist:
            raise Http404
    def get(self, request, api_key):
        city_weather = self.get_object(api_key)
        serializer = WeatherArchiveSerializer(city_weather, many=True, context={"request": request})
        return Response(serializer.data)
    def delete(self, request, api_key, format=None):
        city_weather = self.get_object(api_key)
        city_weather.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

class WeatherNowView(APIView):
    def create_object(self, city_name):

        last_update_timestamp = datetime.now() + timedelta(hours=1)
        city = city_name
        weather = CityWeatherRender.city_name_weather(city_name)
        weather_now_object = {'last_update_timestamp': last_update_timestamp, 'city': city, "weather": weather}
        return weather_now_object

    def get_object(self, city_name):
        try:
            return self.create_object(city_name)
        except Cities.DoesNotExist:
            raise Http404
    def get(self, request, city_name, api_key):
        user = ApiKeys.objects.get(api_key=api_key).user
        if user == None:
            Response(status=status.HTTP_204_NO_CONTENT)
        else:
            city_weather = self.get_object(city_name)
            serializer = WeatherSerializer(city_weather, context={"request": request})
            return Response(serializer.data)
    def delete(self, request, city_name, format=None):
        city_weather = self.get_object(id)
        city_weather.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)