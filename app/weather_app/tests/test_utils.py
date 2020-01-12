from django.core.wsgi import get_wsgi_application
import os
import pytest
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'flight_analyser.settings')
application = get_wsgi_application()
from unittest import TestCase
from acb.utils import sort_by

TEST_DIV_DATA = (
    ([0, 1, 1], 1),
    ([5, 2, 'c'], 'c'),
    ([7, 2, 2], 2),
    ([0, 0, 0], 0),
)

@pytest.mark.parametrize("a, result", TEST_DIV_DATA)
def test_sort_by(a, result):
    assert sort_by(a) == result

# class UtilsTests(TestCase):
#
#     second_element = sort_by([0, 1,2])
#     element_value = 2
#
#
#     def test_sort(self):
#         self.assertEqual(self.second_element, self.element_value)

