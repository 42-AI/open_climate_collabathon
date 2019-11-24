from django.contrib import admin
from .models import DataFile, Maps, States, Projections

admin.site.register(DataFile)
admin.site.register(Maps)
admin.site.register(States)
admin.site.register(Projections)
