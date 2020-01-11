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
        # list_airports = Airports.objects.all()
        return render(request, 'show_cities.html', context={
            'cities_data':cities_data,
        })

class CityWeatherRender(View):
    @method_decorator(login_required)
    def get(self, request, name):
        cities_data = Cities.objects.get(name=name)
        latitude = cities_data.latitude_deg
        longitude = cities_data.longitude_deg
        weather_data_context = WeatherApi.weather_json_restructure(latitude, longitude)

        return render(request, 'rendered_tables/weather_data.html',
                      context=weather_data_context)


#
# class FlightsTableRender(View):
#     @method_decorator(login_required)
#     def get(self, request, airport, data_type, status, isDelay):
#         current_time = date_time_now()
#         data_flight = DataFromApi.flight_table_parameters(airport, data_type, status, isDelay)
#
#         return render(request, 'rendered_tables/generic_table.html',
#                       context={'data_flight': data_flight, 'current_time': current_time})
#
# class AirportExtandedData(View):
#     @method_decorator(login_required)
#     def get(self, request, iata):
#
#         extandet_table_context = DataFromApi.extanded_table(iata)
#
#         return render(request, 'rendered_tables/extend_data.html',
#                       context=extandet_table_context)
#
# class SaveToFlightArchiveView(SuperUserCheck, View):
#     def get(self, request):
#         airport_data = Airports.objects.all()
#
#         return render(request, 'flight_archive/save_flight_archive.html', context={'airport_data': airport_data})
#
#     def post(self, request):
#         airport_selector = request.POST.get('airport')
#         type_selector = request.POST.get('type-selector')
#         canceled_deleyed_selector = request.POST.get('canceled-deleyed-selector')
#
#         FlightArchive.save_to_flight_archive(airport_selector, type_selector, canceled_deleyed_selector)
#
#         return render(request, 'flight_archive/save_flight_archive.html',
#                       context={'airport_selector': airport_selector, 'type_selector': type_selector,
#                                'canceled_deleyed_selector': canceled_deleyed_selector})

# class ViewFlightArchive(View):
#     @method_decorator(login_required)
#     def get(self, request):
#
#         paginator_selector = request.GET.get('paginator-selector')
#         flights_archive_serch = request.GET.get('flights-archive-serch')
#
#         if flights_archive_serch:
#             flights_all = FlightArchive.render_archive_table(flights_archive_serch)
#         else:
#             flights_all = FlightArchive.render_archive_table(None)
#
#         if paginator_selector == None:
#             paginator_selector = 25
#         paginator = Paginator(flights_all, int(paginator_selector))
#         page = request.GET.get('page')
#         flights_all_paginator = paginator.get_page(page)
#
#         return render(request, 'flight_archive/flights_archive_dashboard.html', context={
#             'flights_all': flights_all_paginator, 'flights_archive_serch': flights_archive_serch
#         })

