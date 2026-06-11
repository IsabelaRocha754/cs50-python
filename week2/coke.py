#prompt the user to insert coin
amount_due = 50
#check if the user has inputted at least 50 cents
while amount_due > 0:
    coin = int(input("Insert Coin: "))
    while coin not in [25, 10, 5]:
        print(f"Amount Due: {amount_due}")
        coin = int(input("Insert Coin: "))
    #update amount due
    amount_due -= coin
    if amount_due > 0:
        print(f"Amount Due: {amount_due}")
    else:
        #output change
        print(f"Change Owed: {-amount_due}")