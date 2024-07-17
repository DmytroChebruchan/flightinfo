# flights/models.py
from django.db import models


class Flight(models.Model):
    departure_time = models.DateTimeField()
    arrival_time = models.DateTimeField()
    flight_number = models.CharField(max_length=100)
    destination = models.CharField(max_length=100)

    def __str__(self):
        return self.flight_number
