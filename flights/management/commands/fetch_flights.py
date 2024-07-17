# flights/management/commands/fetch_flights.py
import requests
from bs4 import BeautifulSoup
from django.core.management.base import BaseCommand
from flights.models import Flight
from datetime import datetime, timedelta


class Command(BaseCommand):
    help = 'Fetch flight information from the airport website'

    def handle(self, *args, **kwargs):
        url = 'https://airport.md/ru/passenger/online-panel#departures'
        response = requests.get(url)
        soup = BeautifulSoup(response.text, 'html.parser')

        # Assuming there is a specific HTML structure to target
        # You will need to inspect the structure and adjust accordingly
        flights = []

        for flight_info in soup.select('selector-for-flight-info'): # Adjust this selector
            flight_number = flight_info.select_one('selector-for-flight-number').text
            destination = flight_info.select_one('selector-for-destination').text
            departure_time = datetime.strptime(flight_info.select_one('selector-for-departure-time').text, '%Y-%m-%d %H:%M:%S')

            arrival_time = departure_time + timedelta(hours=2) # Assuming average flight duration
            flights.append(Flight(departure_time=departure_time, arrival_time=arrival_time, flight_number=flight_number, destination=destination))

        Flight.objects.bulk_create(flights)
        self.stdout.write(self.style.SUCCESS('Successfully fetched flight information'))


if __name__ == '__main__':
    Command().handle()
