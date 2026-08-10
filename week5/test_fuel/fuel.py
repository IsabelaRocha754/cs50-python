def main():
    while True:
        fraction = input('Fraction: ')

        try:
            percentage = convert(fraction)
            break
        except(ValueError, ZeroDivisionError):
            continue
 
    result = gauge(percentage)
    if isinstance(result, int):
        print(f"{result}%")
    else:
        print(result)



def convert(fraction):

    x_str, y_str = fraction.split('/')

    x = int(x_str)
    y = int(y_str)

    if y == 0:
        raise ZeroDivisionError
    if x > y or x < 0 or y < 0:
        raise ValueError

    return round((x/y) * 100)


def gauge(percentage):
    if percentage <= 1:
        return "E"
    elif percentage >= 99:
        return "F"
    else:
        return percentage


if __name__ == "__main__":
    main()
