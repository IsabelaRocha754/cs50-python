expression = input("Expression: ")
x = float(expression.rsplit(" ", 2)[0])
y = (expression.rsplit(" ", 2)[1])
z = float(expression.rsplit(" ", 2)[2])

if y == '+':
    print(x+z)
elif y == '-':
    print(x-z)
elif y == '*':
    print(x*z)
elif y == '/':
    print(x/z)