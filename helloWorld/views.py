from django.shortcuts import render
from django.http import JsonResponse
from .models import WEATHER
# Create your views here.


def HOME(request):
    q1 = WEATHER.objects.all().values()
    # print(q1,'\n next')
    # data = JsonResponse(q1,safe =False)
    print(q1)
    return render(request, 'helloWorld/base.html', {'data': q1})
