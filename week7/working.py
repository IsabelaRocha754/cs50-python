import re
import sys


def main():
    print(convert(input("Hours: ")))


def convert(s):
    match = re.search(
        r"^(\d{1,2})(?::([0-5]\d))? (AM|PM) to (\d{1,2})(?::([0-5]\d))? (AM|PM)$", s
    )
    if not match:
        raise ValueError("Invalid format")

    start_h, start_m, start_p, end_h, end_p, end_m = None, None, None, None, None, None
    start_h, start_m, start_p, end_h, end_m, end_p = match.groups()

    start = to_24hr(start_h, start_m, start_p)
    end = to_24hr(end_h, end_m, end_p)

    return f"{start} to {end}"


def to_24hr(hour, minute, period):
    hour = int(hour)
    minute = int(minute) if minute else 0

    if not (1 <= hour <= 12):
        raise ValueError("Hour out of range")

    if period == "AM":
        hour = 0 if hour == 12 else hour
    else:
        hour = 12 if hour == 12 else hour + 12

    return f"{hour:02}:{minute:02}"


if __name__ == "__main__":
    try:
        main()
    except ValueError:
        sys.exit("ValueError")