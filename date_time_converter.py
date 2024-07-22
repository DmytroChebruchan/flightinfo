from datetime import datetime

# Mapping of Russian month abbreviations to English month names
month_mapping = {
    "ЯНВ": "Jan", "ФЕВ": "Feb", "МАР": "Mar", "АПР": "Apr", "МАЙ": "May",
    "ИЮН": "Jun",
    "ИЮЛ": "Jul", "АВГ": "Aug", "СЕН": "Sep", "ОКТ": "Oct", "НОЯ": "Nov",
    "ДЕК": "Dec"
}


def parse_date_time(date_str: str) -> datetime:
    # Split the date_str into time and date parts
    time_str, date_str = date_str.split(maxsplit=1)

    # Extract the day and month abbreviation
    day, month_abbr = date_str.split()

    # Convert month abbreviation to English
    month = month_mapping.get(month_abbr.upper(), "Unknown")

    # Format the date_str into a format that datetime.strptime can understand
    formatted_date_str = f"{day} {month}"

    # Combine time and date parts
    datetime_str = f"{time_str} {formatted_date_str}"

    # Parse the datetime string into a datetime object
    return datetime.strptime(datetime_str, "%H:%M %d %b")


# Example usage
date_str = "00:25 10 ИЮЛ"
parsed_datetime = parse_date_time(date_str)
print(parsed_datetime)
