from django.core.wsgi import get_wsgi_application
import os
import pytest
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'flight_analyser.settings')
application = get_wsgi_application()
from django.test.utils import setup_test_environment
setup_test_environment()
from django.test import Client

c = Client()
# response = c.post('/login/', {'username': 'user', 'password': 'Kamil100!'})
# response.status_code
response = c.get('/')

response.content


