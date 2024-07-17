import requests
from bs4 import BeautifulSoup
from django.core.management.base import BaseCommand
from flights.models import Flight
from datetime import datetime, timedelta

class Command(BaseCommand):
    help = 'Fetch flight information from the airport website'

    def handle(self, *args, **kwargs):
        url = 'https://airport.md/ru/passenger/online-panel#departures'
        response = requests.get(url, verify=False)
        soup = BeautifulSoup(response.text, 'html.parser')

        flights = []

        for flight_info in soup.find_all('div', class_='tr'):
            flight_number = flight_info.find('div', class_='td col-xs-3 col-sm-2 col-md-2').text.strip()
            destination = flight_info.find('div', class_='td col-xs-4 col-sm-4 col-md-4').text.strip().split('(')[0].strip()
            scheduled_departure = flight_info.find('div', class_='sch').text.strip()

            # Extract date and time from the scheduled_departure
            scheduled_time_str = scheduled_departure.split(',')[0].strip()
            scheduled_date_str = scheduled_departure.split(',')[1].strip()

            scheduled_datetime_str = f"{scheduled_time_str}, {scheduled_date_str}"
            departure_time = datetime.strptime(scheduled_datetime_str, '%H:%M, %d %b')

            # Assuming an average flight duration for arrival time
            arrival_time = departure_time + timedelta(hours=2)

            flights.append(Flight(departure_time=departure_time, arrival_time=arrival_time, flight_number=flight_number, destination=destination))
            print(flight_info)
        # Flight.objects.bulk_create(flights)
        self.stdout.write(self.style.SUCCESS('Successfully fetched flight information'))

