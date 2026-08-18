import sys

argc = len(sys.argv)
argv = sys.argv

if argc < 2:
    print("Too few command-line arguments")
    sys.exit(1)
elif argc > 2:
    print("Too many command-line arguments")
    sys.exit(1)

if argv[1].endswith(".py") == False:
    print("Not a python file")
    sys.exit(1)

file = argv[1]

number_of_lines = 0

try:
    with open(file, "r") as file:
        for line in file:
            current_line = line.strip()
            if current_line.startswith("#") or current_line == "":
                continue
            else:
                number_of_lines += 1
except FileNotFoundError:
    print("File not found")
    sys.exit(1)

print(number_of_lines)
