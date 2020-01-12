from django.core.wsgi import get_wsgi_application
import os
import pytest

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'flight_analyser.settings')
application = get_wsgi_application()

import unittest
from django.test import Client


class UrlConnection(unittest.TestCase):
    def setUp(self):
        # Every test needs a client.
        self.client = Client()

    def test_correct_example(self):
        lat = 10
        lon = 10

        # Issue a GET request.
        response = self.client.get(f'/airport_extendet_data_table/{lat}/{lon}/')

        # Check that the response is 200 OK.
        self.assertEqual(response.status_code, 200)


from acb.weather_api import WeatherApi

TEST_DIV_DATA = (
    (10, 10, 10),
)


@pytest.mark.parametrize("lat, lon, result", TEST_DIV_DATA)
def test_weather_Api(lat, lon, result):
    assert WeatherApi.connect_to_api(lat, lon)['coord']['lat'] == result
    assert WeatherApi.connect_to_api(lat, lon)['coord']['lon'] == result





