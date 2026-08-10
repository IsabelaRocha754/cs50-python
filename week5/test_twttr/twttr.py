def main():
    prompt = input("Input: ")

    no_vowels = shorten(prompt)

    print(f"Output: {no_vowels}")


def shorten(word):
    no_vowels = ''

    for letter in word:
        if letter.lower() not in 'aeiou':
            no_vowels += letter

    return no_vowels




if __name__ == "__main__":
    main()
