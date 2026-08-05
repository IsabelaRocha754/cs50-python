import random

while True:
    try:
        level = int(input("Level: "))
        if level <= 0:
            raise ValueError
        else:
            break
    except ValueError:
        continue

chosen = random.randint(1, level)

while True:
    try:
        guess = int(input("Guess: "))

        if guess <= 0:
            raise ValueError
        elif guess > chosen:
            print("Too large!")
            raise ValueError
        elif guess < chosen:
            print("Too small!")
            raise ValueError
        else:
            print("Just right!")
            break
    except ValueError:
        continue
