# flights/views.py
from datetime import timedelta

from django.shortcuts import render
from django.utils import timezone

from search import collect_flights_script


def flights_per_hour(request):
    current_time = timezone.now()
    end_time = current_time + timedelta(hours=24)

    flights = collect_flights_script()

    hours = [current_time + timedelta(hours=i) for i in range(24)]
    flight_counts = {hour: 0 for hour in hours}

    for flight in flights:
        arrival_hour = flight.arrival_time.replace(
            minute=0, second=0, microsecond=0
        )
        if arrival_hour in flight_counts:
            flight_counts[arrival_hour] += 1

    context = {"flight_counts": sorted(flight_counts)}

    return render(request, "flights/flights_per_hour.html", context)
