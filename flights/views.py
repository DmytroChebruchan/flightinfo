from django.shortcuts import render

from flights.additional_functions import flight_counts_generator


def flights_per_hour(request):
    context = {"flight_counts": flight_counts_generator(),
               "recommended_gap": 1}
    return render(request, "flights/flights_per_hour.html", context)


def flight_number_collector(request):
    return render(request, "flights/flight_number_collector.html")


