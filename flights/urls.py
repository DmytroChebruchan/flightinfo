# flights/urls.py
from django.urls import path

from .views import flights_per_hour, flight_number_collector

urlpatterns = [
    path("", flights_per_hour, name="flights_per_hour"),
    path("flight_number_collector/", flight_number_collector, name="flight_number_collector"),
]
