import sys
from tabulate import tabulate

argc = len(sys.argv)
argv = sys.argv

if argc < 2:
    print("Too few command-line arguments")
    sys.exit(1)
elif argc > 2:
    print("Too many command-line arguments")
    sys.exit(1)

if argv[1].endswith(".csv") == False:
    print("Not a CSV file")
    sys.exit(1)

file = argv[1]

items = []

try:
    with open(file) as file:
        headers = file.readline().rstrip().split(",")
        for line in file:
            items.append(line.rstrip().split(","))
except FileNotFoundError:
    print("File not found")
    sys.exit(1)

print(tabulate(items, headers=headers, tablefmt="grid"))