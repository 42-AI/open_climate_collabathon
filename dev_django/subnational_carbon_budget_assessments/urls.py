from django.contrib import admin
from django.urls import include, path
from . import views
from map.views import MapsView, StatesView, SeriesView, PointsView

urlpatterns = [
    path('', views.index, name='index'),
    path('maps/', MapsView.as_view(), name="maps"),
    path('maps/<str:country>', StatesView.as_view(), name="states"),
    path('states/<str:state>', SeriesView.as_view(), name="series"),
    path('series/<str:serie>', PointsView.as_view(), name="points"),
    path('admin/', admin.site.urls),
    path('api/', include('map.urls')),
]