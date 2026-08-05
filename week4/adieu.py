import inflect
p = inflect.engine()

people = []

while True:
    try:
        name = input("Name: ")
        people.append(name)
    except EOFError:
        print()
        break
print(f"Adieu, adieu, to {p.join(people)}")