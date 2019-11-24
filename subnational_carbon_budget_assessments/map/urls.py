from django.contrib import admin
from django.urls import path, re_path, include

from . import views
from .views import ListMapsView, ListStatesView, ListProjectionsView

urlpatterns = [
    path('', views.index, name='api'),
    path('maps/', ListMapsView.as_view(), name="maps"),
    path('maps/<str:country>', ListStatesView.as_view(), name="states"),
    path('projections/<str:state>', ListProjectionsView.as_view(), name="projections"),
]