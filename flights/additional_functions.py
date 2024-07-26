from datetime import timedelta

from django.utils import timezone

from search import collect_flights_script


def is_delta_less_than_one_hour(datetime1, datetime2):
    # Calculate the difference between the two datetimes
    delta = abs(datetime1 - datetime2)

    # Compare the delta with a timedelta of one hour
    return delta < timedelta(hours=1, minutes=30)


def flight_counts_generator():
    flight_time = timezone.now()

    flights = collect_flights_script()
    flight_counts = 0
    for flight in flights:
        print(is_delta_less_than_one_hour(flight_time,
                                          flight["scheduled_departure"]))
        if is_delta_less_than_one_hour(flight_time,
                                       flight["scheduled_departure"]):
            flight_counts[flight.departure_time.hour] += 1
    return flight_counts
