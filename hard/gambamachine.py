def deposit():
    while True:
        amount = input("Enter amount to deposit: ")
        if amount > 0 and amount.isdigit():
            amount = int(amount)
        else:
            print("deposit must be greater then zero!! ")
            break
    return amount

 