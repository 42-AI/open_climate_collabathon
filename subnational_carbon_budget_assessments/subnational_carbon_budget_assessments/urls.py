from django.contrib import admin
from django.urls import include, path
from . import views

from rest_framework import routers
from map.views import MapViewSet

router = routers.DefaultRouter()
router.register(r'api/map', MapViewSet, base_name='map')

urlpatterns = [
    path('', views.index, name='index'),
    path('admin/', admin.site.urls),
]

urlpatterns += router.urls