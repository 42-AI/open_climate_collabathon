from django.urls import path

from . import views
from .views import MapView

urlpatterns = [
    path('', views.index, name='index'),
    path('US', MapView.as_view(),name='map'),
]
