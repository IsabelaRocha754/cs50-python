def main():
    plate = input("Plate: ")
    if is_valid(plate):
        print("Valid")
    else:
        print("Invalid")


def is_valid(s):
    valid = False
    
    #start with two letter, min of 2 and max of 6 characters
    if 2 <= len(s) <= 6 and s[0].isalpha() and s[1].isalpha():
        valid = True
    
    #numbers not in the middle
    for i in range(len(s) - 1):
        if not s[i].isalpha():
            if s[i+1].isalpha():
                valid = False
    
    #no periods, spaces, or punctuation marks
    for letter in s:
        if not letter.isalnum():
            valid = False
    
    #first number cannot be 0
    number = False
    for char in s:
        if number == False and char.isdigit():
            number = True
            if char == '0':
                valid = False


    return valid

main()