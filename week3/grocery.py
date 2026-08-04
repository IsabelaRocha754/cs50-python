import sys

grocery = {}

try:
    while True:
        item = input('').upper()

        if item not in grocery:
            grocery[item] = 1
        else:
            grocery[item] += 1
except EOFError:
    for item, quantity in sorted(grocery.items()):
        print(quantity, item)
    sys.exit()