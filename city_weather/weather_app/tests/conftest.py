from django.core.wsgi import get_wsgi_application
import os
import pytest

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'flight_analyser.settings')
application = get_wsgi_application()

from acb.models import AirportsAllData


@pytest.fixture
def airports_all_data_single_object_test():
    single_object_test = AirportsAllData.objects.create(type='medium_airport',
                                                        name='Kugluktuk Airport',
                                                        latitude_deg='67.816704',
                                                        longitude_deg='-115.143997',
                                                        elevation_ft='74',
                                                        iso_country='CA',
                                                        iso_region='CA-NU',
                                                        municipality='Kugluktuk',
                                                        gps_code='CYCO',
                                                        iata_code ='YCO',
                                                        local_code='',
                                                        home_link='',
                                                        wikipedia_link='https://en.wikipedia.org/wiki/Kugluktuk_Airport',
                                                        country_name='Canada',
                                                        isEEA='False')


    return single_object_test
