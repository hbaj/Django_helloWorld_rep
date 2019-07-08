from django.db import models

# Create your models here.


class WEATHER(models.Model):
    Pressure = models.IntegerField()
    Temperature = models.IntegerField()

    def __str__(self):
        return "WEATHER_STR"

    class Meta:
        verbose_name = "Weather"
        verbose_name_plural = "Weather"
