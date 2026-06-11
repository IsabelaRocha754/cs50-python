prompt = input("Input: ")

print("Output: ", end="")
for letter in prompt:
    if letter.lower() not in 'aeiou':
        print(letter, end="")

print()