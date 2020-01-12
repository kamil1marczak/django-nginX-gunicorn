"""flight_analyser URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""

from django.contrib import admin
from django.urls import path, re_path
from weather_app.views import *
from weather_app.views_authentication import *

from weather_app.init_settings import *
from weather_app.weather_api import *
from weather_app.views_initial import CreateUser, InitialData
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('login/', LoginView.as_view(), name='login'),
    path('logout/', LogoutView.as_view(), name='logout'),
    path('', IndexView.as_view(), name='dashboard'),
    path('show_weather/', CityWeatherMain.as_view()),

    path('initial_user/', CreateUser.as_view()),
    path('initial_data/', InitialData.as_view()),
    path('city_weather/<str:name>/', CityWeatherRender.as_view()),

    path('airport_extendet_data_table/<str:lat>/<str:lon>/', WeatherData.as_view()),

    path('save_weather_archive/', SaveToWeatherArchiveView.as_view()),
    path('weather_archive_dashboard/', ViewWeatherArchive.as_view()),


] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
