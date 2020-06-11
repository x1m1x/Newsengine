from django.urls import path

from .views import *

urlpatterns = [
    path('', city_list, name="city_list_url"),
    path('cities/delete/', cities_delete, name="cities_delete_url"),
]
