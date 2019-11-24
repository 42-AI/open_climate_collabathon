from django.contrib import admin
from django.urls import path, re_path, include

from . import views
from .views import ListMapsView, ListStatesView, ListSeriesView, ListPointsView

urlpatterns = [
    path('', views.index, name='api'),
    path('maps/', ListMapsView.as_view(), name="maps"),
    path('maps/<str:country>', ListStatesView.as_view(), name="states"),
    path('state/<str:state>', ListSeriesView.as_view(), name="series"),
    path('series/<str:serie>', ListPointsView.as_view(), name="points"),
]