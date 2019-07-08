from django.contrib import admin
from .models import WEATHER
# Register your models here.


class WEATHERAdmin(admin.ModelAdmin):
    list_display = ('id', 'Pressure', 'Temperature')


admin.site.register(WEATHER, WEATHERAdmin)
