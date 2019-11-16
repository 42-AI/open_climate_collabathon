from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('US', views.MapView.as_view(),name='map'),
]
