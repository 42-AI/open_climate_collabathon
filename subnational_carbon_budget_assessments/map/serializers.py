from rest_framework import serializers
from .models import Maps, States, Series, Points

class MapsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Maps
        fields = ("country",)

class StatesSerializer(serializers.ModelSerializer):
    class Meta:
        model = States
        fields = ("country", "state")

class SeriesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Series
        fields = ("state", "serie")

class PointsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Points
        fields = ("serie", "year", "data")