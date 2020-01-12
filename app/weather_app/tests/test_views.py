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

    def test_main_page(self):
        # Issue a GET request.
        response = self.client.get('/')

        # Check that the response is 200 OK.
        self.assertEqual(response.status_code, 200)

        # Check that the rendered context contains 5 customers.
        # self.assertEqual(len(response.context['customers']), 5)

    def test_incorect_page(self):
        response = self.client.get('/test/test/test')
        self.assertEqual(response.status_code, 404)
