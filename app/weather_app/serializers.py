from weather_app.models import Cities, WeatherArchive
from rest_framework import serializers
from django.contrib.postgres.fields import JSONField

class CitiesSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Cities
        fields = ["id", "name", "latitude_deg", "longitude_deg", "country"]


class WeatherArchiveSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = WeatherArchive
        fields = ["last_update_timestamp", "city", "weather"]

class WeatherSerializer(serializers.Serializer):
    last_update_timestamp = serializers.CharField(read_only=True)
    city = serializers.CharField(read_only=True)
    weather =serializers.JSONField()