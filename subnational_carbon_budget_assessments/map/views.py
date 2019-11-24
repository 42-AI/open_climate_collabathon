from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render

def index(request):
    return HttpResponse("Hello world. You are at the map index.")

##### API #####
from rest_framework import generics
from .models import Maps, States, Series, Points
from .serializers import MapsSerializer, StatesSerializer, SeriesSerializer, PointsSerializer

class ListMapsView(generics.ListAPIView):
    """
    Provides a get method handler.
    """
    queryset = Maps.objects.all()
    serializer_class = MapsSerializer

class ListStatesView(generics.ListAPIView):
    """
    Provides a get method handler.
    """
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
    """
    Provides a get method handler.
    """
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
    """
    Provides a get method handler.
    """
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