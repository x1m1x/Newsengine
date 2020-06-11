import requests

from django.shortcuts import render, reverse
from django.views.generic import View
from django.http import HttpResponseRedirect

from .models import City
from .forms import CityForm


def city_list(request):
    api = "5b274d330ba264c14d945d8e27baf879"
    url = "https://api.openweathermap.org/data/2.5/weather?q={}&units=metric&appid=" + api

    if request.method == "POST":
        form = CityForm(request.POST)
        if form.is_valid():
            form.save()

    form = CityForm()

    cities = City.objects.all()

    all_info = []

    for city in cities:
        try:
            res = requests.get(url.format(city.name)).json()

            city_info = {
                'city': city.name,
                'temp': res["main"]["temp"],
                'icon': res["weather"][0]["icon"]
            }
            all_info.append(city_info)
        except:
            City.objects.get(name=city.name).delete()

    context = {
        'all_info': all_info,
        'form': form
    }

    return render(request, 'weather/city_list.html', context)

def cities_delete(request):
    cities = City.objects.all()
    cities.delete()

    return HttpResponseRedirect(reverse('city_list_url'))
