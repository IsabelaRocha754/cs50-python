def main():
    time = input("What time is it? ")

    if 7.0 <= convert(time) <= 8.0:
        print("breakfast time")
    elif 12.0 <= convert(time) <= 13.0:
        print("lunch time")
    elif 18.0 <= convert(time) <= 19.0:
        print("dinner time")

def convert(time):
    min = float(time.rsplit(":", 1)[1])/60
    hour = float(time.rsplit(":", 1)[0])

    return (hour+min)


if __name__ == "__main__":
    main()