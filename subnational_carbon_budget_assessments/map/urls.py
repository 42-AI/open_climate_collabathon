from django.contrib import admin
from django.urls import path, re_path, include

from . import views
from .views import ListMapsView, ListStatesView, ListSeriesView, ListPointsView

urlpatterns = [
    path('', views.index, name='api'),
    path('maps/', ListMapsView.as_view(), name="api_maps"),
    path('maps/<str:country>', ListStatesView.as_view(), name="api_states"),
    path('states/<str:regionName>', ListSeriesView.as_view(), name="api_series"),
    path('series/<str:serie>', ListPointsView.as_view(), name="api_points"),
]