months = [
    "january",
    "february",
    "march",
    "april",
    "may",
    "june",
    "july",
    "august",
    "september",
    "october",
    "november",
    "december"
]


while True:
    date_before = input("Date: ").lower()
    try:
        if "/" in date_before:
            month = int(date_before.split('/')[0])
            day = int(date_before.split('/')[1])
            year = int(date_before.split('/')[2])
        elif "," in date_before:
            month = months.index(date_before.split()[0]) + 1
            day = int(date_before.split()[1].replace(',', ''))
            year = int(date_before.split()[2])
        else:
            raise ValueError

        if month < 1 or month > 12 or day < 1 or day > 31:
            raise ValueError

        break
    except (ValueError, IndexError):
        continue

print(f"{year}-{month:02}-{day:02}")