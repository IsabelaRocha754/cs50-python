answer = input("What is the Answer to the Great Question of Life, the Universe, and Everything? ").replace(" ", "")
if answer == "42" or answer.lower() == "forty-two" or answer.lower() == "fortytwo":
    print("Yes")
else:
    print("No")