import sys
from datetime import date
import inflect


def main():
    dob = input("Date of Birth: ")
    birth_date = parse_date(dob)
    minutes = minutes_since(birth_date)
    print(format_minutes(minutes))


def parse_date(date_string):
    try:
        year, month, day = date_string.split("-")
        return date(int(year), int(month), int(day))
    except ValueError:
        sys.exit("Invalid date")


def minutes_since(birth_date):
    today = date.today()
    delta = today - birth_date
    return round(delta.days * 24 * 60)


def format_minutes(minutes):
    p = inflect.engine()
    words = p.number_to_words(minutes, andword="")
    return f"{words.capitalize()} minutes"


if __name__ == "__main__":
    main()
