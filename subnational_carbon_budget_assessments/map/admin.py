from django.contrib import admin
from .models import DataFile, Maps, States, Series, Points

admin.site.register(DataFile)
admin.site.register(Maps)
admin.site.register(States)
admin.site.register(Series)
admin.site.register(Points)
