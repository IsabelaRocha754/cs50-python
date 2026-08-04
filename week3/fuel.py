def main():
    while True:
        fraction = input("Fraction: ")
        percentage = convert(fraction)

        if percentage is not None:
            break

    if percentage <= 1:
        print('E')
    elif percentage >= 99:
        print('F')
    else:
        print(f'{percentage}%')

def convert(fraction):
    try:
        x_str, y_str = fraction.split('/')

        x = int(x_str)
        y = int(y_str)

        if y == 0:
            raise ZeroDivisionError
        if x > y or x < 0 or y < 0:
            raise ValueError

        return round((x/y) * 100)
    except (ValueError, ZeroDivisionError):
        return None

main()