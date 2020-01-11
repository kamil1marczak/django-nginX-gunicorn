from django.views import View
from django.shortcuts import render

import json
from datetime import datetime, timedelta
from weather_app.weather_api import WeatherApi


# class FlightArchive:
#     @staticmethod
#     def save_to_flight_archive(airport_selector, type_selector, canceled_deleyed_selector):
#         airport = airport_selector
#         data_type = type_selector
#         canceled_deleyed_selector_jeson = json.loads(canceled_deleyed_selector)
#         status = canceled_deleyed_selector_jeson['status']
#         isDelay = canceled_deleyed_selector_jeson['isDelay']
#
#         flight_archive_creator = DataFromApi.flight_table_parameters(airport, data_type, status, isDelay)
#
#         for table_data in flight_archive_creator:
#
#             lat_departure = Airports.objects.get(iata_code=table_data['departure']['iataCode']).latitude_deg
#             lon_departure = Airports.objects.get(iata_code=table_data['departure']['iataCode']).longitude_deg
#
#             weather_departure = WeatherApi.connect_to_api(lat_departure, lon_departure)
#
#             lat_arrival = Airports.objects.get(iata_code=table_data['departure']['iataCode']).latitude_deg
#             lon_arrival = Airports.objects.get(iata_code=table_data['departure']['iataCode']).longitude_deg
#
#             weather_arrival = WeatherApi.connect_to_api(lat_arrival, lon_arrival)
#
#             try:
#                 codesharing_icao_number = table_data['codeshared']['airline']['icaoCode']
#                 codesharing_name = table_data['codeshared']['airline']['name']
#             except:
#                 codesharing_icao_number = 'None'
#                 codesharing_name = 'None'
#
#             if table_data['departure']['actualTime'] == None:
#                 departure_actual_estimatedtime = table_data['departure']['scheduledTime']
#             else:
#                 departure_actual_estimatedtime = table_data['departure']['actualTime']
#
#             if table_data['arrival']['actualTime'] == None:
#                 arrival_actual_estimatedtime = table_data['arrival']['scheduledTime']
#             else:
#                 arrival_actual_estimatedtime = table_data['arrival']['actualTime']
#
#             try:
#                 line_to_update = Flights_archive.objects.get(departure_airport_iata=table_data['departure']['iataCode'],
#                                                              departure_scheduledtime=table_data['departure'][
#                                                                  'scheduledTime'],
#                                                              flight_icao=table_data['flight']['icaoNumber'])
#             except:
#                 line_to_update = None
#
#             if line_to_update == None:
#                 Flights_archive.objects.create(last_update_timestamp=datetime.now() + timedelta(hours=1),
#                                                departure_airport_iata=Airports.objects.get(
#                                                    iata_code=table_data['departure']['iataCode']),
#                                                departure_weather=weather_departure,
#                                                departure_scheduledtime=table_data['departure']['scheduledTime'],
#                                                departure_actual_estimatedtime=departure_actual_estimatedtime,
#                                                arrival_airport_iata=Airports.objects.get(
#                                                    iata_code=table_data['arrival']['iataCode']),
#                                                arrival_weather=weather_arrival,
#                                                arrival_scheduledtime=table_data['arrival']['estimatedTime'],
#                                                arrival_actual_estimatedtime=arrival_actual_estimatedtime,
#                                                flight_icao=table_data['flight']['icaoNumber'],
#                                                airline_icao_number=table_data['airline']['icaoCode'],
#                                                airline_name=table_data['airline']['name'],
#                                                codesharing_icao_number=codesharing_icao_number,
#                                                codesharing_name=codesharing_name)
#
#             else:
#                 line_to_update.last_update_timestamp = datetime.now() + timedelta(hours=1)
#                 line_to_update.departure_weather = weather_departure
#                 # line_to_update.departure_scheduledtime=table_data['departure']['scheduledTime'],
#                 line_to_update.departure_actual_estimatedtime = departure_actual_estimatedtime
#                 # line_to_update.arrival_airport_iata=table_data['arrival']['iataCode'],
#                 line_to_update.arrival_weather = weather_arrival
#                 # line_to_update.arrival_scheduledtime=table_data['arrival']['estimatedTime'],
#                 line_to_update.arrival_actual_estimatedtime = arrival_actual_estimatedtime
#                 # line_to_update.airline_iatanumber=table_data['flight']['iataNumber'],
#                 # line_to_update.codesharing_iatanumber=codesharing_iatanumber
#                 line_to_update.save()
#
#         message = 'data added to db'
#
#         return render(request, 'flight_archive/save_flight_archive.html', context={'message': message})
#
#     def render_archive_table(serch):
#         if serch == None:
#             flights_all = Flights_archive.objects.all()
#         else:
#             flights_all = Flights_archive.objects.filter(departure_airport_iata=serch)
#
#         for flights in flights_all:
#             try:
#                 duration_departure = (flights.departure_actual_estimatedtime - flights.departure_scheduledtime)
#                 duration_in_s_departure = duration_departure.total_seconds()
#                 departure_delay = divmod(duration_in_s_departure, 60)[0]
#                 departure_delay = round(departure_delay)
#
#                 if departure_delay < 0.1:
#                     departure_delay = None
#             except:
#                 departure_delay = None
#             flights.departure_delay = departure_delay
#
#             try:
#                 duration_arrival = flights.arrival_actual_estimatedtime - flights.arrival_scheduledtime
#                 duration_in_s_arrival = duration_arrival.total_seconds()
#                 arrival_delay = divmod(duration_in_s_arrival, 60)[0]
#                 arrival_delay = round(arrival_delay)
#
#                 if arrival_delay < 0.1:
#                     arrival_delay = None
#             except:
#                 arrival_delay = None
#             flights.arrival_delay = arrival_delay
#
#         return flights_all





