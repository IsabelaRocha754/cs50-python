#prompt the user for camelCase
camel = input("camelCase: ")
#check if there is upper case
def upper_case(name):
    upper = False
    for i in range(len(camel)):
        if camel[i].isupper():
            upper = True
            return upper
#split the camelCase where the upper case is
while upper_case(camel):
    for i in range(len(camel)):
        if camel[i].isupper():
            first = camel[:i]
            second = camel[i:]
#add an underscore and transform the upper case in lower case
            camel = first + '_' + second[0].lower() + second[1:]
            upper_case(camel)
#print snake_case
print(camel)