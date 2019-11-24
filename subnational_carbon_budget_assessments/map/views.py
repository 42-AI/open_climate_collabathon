import json
from django.core import serializers
from django.views import View
from django.http import HttpResponse, HttpResponseRedirect, JsonResponse
from django.shortcuts import render

from .models import Maps, States, Series, Points

from django.core.serializers.json import Serializer
class JSONSerializer(Serializer):
    def get_dump_object(self, obj):
        self._current[obj._meta.pk.name] = obj._get_pk_val()
        return self._current

def index(request):
    return HttpResponse("Hello world. You are at the map index.")

class MapsView(View):
    maps_list_json = None
    def get(self, request, *args, **kwargs):
        if request.method == "GET":
            maps_list = Maps.objects.all()
            maps_list_json = JSONSerializer().serialize(maps_list)
        return render(request, 'maps.html', {"maps_list": maps_list_json})

class StatesView(View):
    def get(self, request, *args, **kwargs):
        states_list_json = None
        if request.method == "GET":
            country = kwargs["country"]
            country_id = Maps.objects.get(country=country).id
            states_list = States.objects.filter(country=country_id)
            states_list_json = JSONSerializer().serialize(states_list, fields=["state"])
        return render(request, 'states.html', {"states_list": states_list_json})

class SeriesView(View):
    def get(self, request, *args, **kwargs):
        series_list_json = None
        if request.method == "GET":
            state = kwargs["state"]
            state_id = States.objects.get(state=state).id
            series_list = Series.objects.filter(state=state_id)
            series_list_json = JSONSerializer().serialize(series_list, fields=["serie"])
        return render(request, 'series.html', {"series_list": series_list_json})

class PointsView(View):
    def get(self, request, *args, **kwargs):
        points_list_json = None
        if request.method == "GET":
            serie = kwargs["serie"]
            serie_id = Series.objects.get(serie=serie).id
            points_list = Points.objects.filter(serie=serie_id)
            points_list_json = JSONSerializer().serialize(points_list, fields=["year", "data"])
        return render(request, 'serie.html', {"points_list": points_list_json})

##### API #####
from rest_framework import generics
from .serializers import MapsSerializer, StatesSerializer, SeriesSerializer, PointsSerializer

class ListMapsView(generics.ListAPIView):
    queryset = Maps.objects.all()
    serializer_class = MapsSerializer

class ListStatesView(generics.ListAPIView):
    serializer_class = StatesSerializer
    def get_queryset(self):
            """
            Optionally restricts the returned states to a given country,
            by filtering against a `country` query parameter in the URL.
            """
            queryset = States.objects.all()
            country = self.kwargs['country']
            if country is not None:
                country_id = Maps.objects.get(country=country).id
                queryset = queryset.filter(country=country_id)
            return queryset

class ListSeriesView(generics.ListAPIView):
    serializer_class = SeriesSerializer
    def get_queryset(self):
            """
            Optionally restricts the returned serie to a given state,
            by filtering against a `state` query parameter in the URL.
            """
            queryset = Series.objects.all()
            state = self.kwargs['state']
            if state is not None:
                state_id = States.objects.get(state=state).id
                queryset = queryset.filter(state=state_id)
            return queryset

class ListPointsView(generics.ListAPIView):
    serializer_class = PointsSerializer
    def get_queryset(self):
            """
            Optionally restricts the returned serie to a given state,
            by filtering against a `state` query parameter in the URL.
            """
            queryset = Points.objects.all()
            serie = self.kwargs['serie']
            if serie is not None:
                serie_id = Series.objects.get(serie=serie).id
                queryset = queryset.filter(serie=serie_id)
            return queryset