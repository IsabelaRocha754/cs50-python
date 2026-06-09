def convert(str):
    if ":)" in str:
        str = str.replace(":)", "🙂")
    if ":(" in str:
        str = str.replace(":(", "🙁")
    return str

def main():
    phrase = input()
    print(convert(phrase))

main()