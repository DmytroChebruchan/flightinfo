from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.firefox.options import Options

from date_time_converter import parse_date_time


def requests_get():
    options = Options()
    options.headless = True
    driver = webdriver.Firefox(options=options)
    driver.get(
        "https://airport.md/ru/passenger/"
        "online-panel?cheeckin-warn#departures"
    )
    driver.find_element(By.CSS_SELECTOR, ".swal2-confirm").click()
    # driver.close()
    return driver


def collecting_flights(cleaned_rows):
    flights_collected = []
    for row in cleaned_rows:
        try:
            flight_info = parse_flight_info(row)
            flights_collected.append(flight_info)
        except:
            pass

    # Print all collected flight information
    print(flights_collected)
    return flights_collected


def find_element_text(row: WebElement, selector: str, default: str = "N/A") -> str:
    elements = row.find_elements(By.CSS_SELECTOR, selector)
    return elements[0].text if elements else default


def parse_flight_info(row: WebElement) -> dict:
    DESTINATION_CLASSES = ".td, .col-xs-4, .col-sm-4, .col-md-4"
    flight_info = {
        "flight_number": find_element_text(row, ".td"),
        "destination": find_element_text(row, DESTINATION_CLASSES),
        "scheduled_departure": parse_date_time(find_element_text(row, ".sch")),
    }
    return flight_info


def cleaning_rows(rows):
    cleaned_rows = []
    for row in rows:
        if row.text != "":
            cleaned_rows.append(row)
    return cleaned_rows


def collect_flights_script():
    driver = requests_get()
    rows = driver.find_elements(By.CSS_SELECTOR, ".row")
    cleaned_rows = cleaning_rows(rows)
    flights_collected = collecting_flights(cleaned_rows)

    return flights_collected
