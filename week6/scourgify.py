import sys
import csv

argc = len(sys.argv)
argv = sys.argv

if argv[1].endswith(".csv") == False or argv[2].endswith(".csv") == False:
    print("Not a CSV file")
    sys.exit(1)

read_file = argv[1]
write_file = argv[2]

students = []

try:
    with open(read_file) as file:
        reader = csv.DictReader(file)
        for row in reader:
            first = row["name"].split(",")[1].strip()
            last = row["name"].split(",")[0].strip()
            students.append({"first": first, "last": last, "house": row["house"]})

    with open(write_file, "w") as file:
        writer = csv.DictWriter(file, fieldnames=["first", "last", "house"])
        writer.writeheader()
        for student in students:
            writer.writerow(student)
except FileNotFoundError:
    print("Could not read")
    sys.exit(1)
