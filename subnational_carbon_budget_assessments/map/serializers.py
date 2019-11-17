from rest_framework import serializers
from .models import Maps, States, Projections

class MapsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Maps
        fields = ("country",)

class StatesSerializer(serializers.ModelSerializer):
    class Meta:
        model = States
        fields = ("country", "state")


class ProjectionsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Projections
        fields = ("state", "data")