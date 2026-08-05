from pyfiglet import Figlet, FontNotFound
import sys

figlet = Figlet()

argc = len(sys.argv)
argv = sys.argv

if argc != 1 and argc != 3:
    print("Invalid Usage")
    sys.exit(1)

if argc == 3:
    if argv[1] == '-f' or argv[1] == '--f':
        try:
            figlet.setFont(font=argv[2])
        except FontNotFound:
            print("Invalid Usage")
            sys.exit(1)
    else:
        print("Invalid Usage")
        sys.exit(1)

input = input("Input: ")
output = figlet.renderText(input)
print("Output: ")
print(output)