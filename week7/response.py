from validator_collection import checkers

# Returns True or False
is_email_valid = checkers.is_email(input("What's your email address? "))
if (is_email_valid):
    print("Valid")
else:
    print("Invalid")
