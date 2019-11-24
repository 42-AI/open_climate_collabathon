from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render

def index(request):
    return HttpResponse("Hello world. You are at the map index.")

##### API #####
from rest_framework import generics
from .models import Maps, States, Projections
from .serializers import MapsSerializer, StatesSerializer, ProjectionsSerializer

class ListMapsView(generics.ListAPIView):
    """
    Provides a get method handler.
    """
    serializer_class = MapsSerializer

    queryset = Maps.objects.all()

class ListStatesView(generics.ListAPIView):
    """
    Provides a get method handler.
    """
    serializer_class = MapsSerializer

    def get_queryset(self):
            """
            Optionally restricts the returned states to a given country,
            by filtering against a `country` query parameter in the URL.
            """
            queryset = States.objects.all()
            country = self.request.query_params.get('country', None)
            if country is not None:
                queryset = queryset.filter(state__country=country)
            return queryset

class ListProjectionsView(generics.ListAPIView):
    """
    Provides a get method handler.
    """
    serializer_class = ProjectionsSerializer

    def get_queryset(self):
            """
            Optionally restricts the returned projection to a given state,
            by filtering against a `state` query parameter in the URL.
            """
            queryset = Projections.objects.all()
            state = self.request.query_params.get('state', None)
            if state is not None:
                queryset = queryset.filter(projections__state=state)
            return queryset