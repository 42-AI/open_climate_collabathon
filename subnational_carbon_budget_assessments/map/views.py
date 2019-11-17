from django.http import HttpResponse

def index(request):
    return HttpResponse("Hello world. You are at the map index.")

from rest_framework.response import Response
from rest_framework import viewsets, status

from . import serializers
from .Map import Map

maps = {
    1: Map(id=1, name='US'),
    2: Map(id=2, name='France'),
    3: Map(id=3, name='Whatever'),
}

class MapViewSet(viewsets.ViewSet):
    # Required for the Browsable API renderer to have a nice form.
    serializer_class = serializers.MapSerializer

    def list(self, request):
        serializer = serializers.MapSerializer(
            instance=maps.values(), many=True)
        return Response(serializer.data)