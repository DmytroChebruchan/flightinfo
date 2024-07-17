# flights/urls.py
from django.urls import path
from .views import flights_per_hour

urlpatterns = [
    path('', flights_per_hour, name='flights_per_hour'),
]
