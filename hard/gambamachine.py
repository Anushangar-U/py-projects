MAX_LINES = 3
MAX_BET = 10000
MIN_BET = 1000

def deposit():
    while True:
        amount = input("Enter amount to deposit: ")
        if amount > 0 and amount.isdigit():
            amount = int(amount)
        else:
            print("deposit must be greater then zero!! ")
            break
    return amount

def get_number_of_lines():
    while True:
        lines = input(f"Enter the number of lines(1 to {MAX_LINES}): ")
        if lines >= 1 and lines<= MAX_LINES:
            lines = int(lines)
        else:
            print("Enter a valid number of lines")
            break
    return lines

def get_bet():
    while True:
        amount = input(f"Enter the amount you want to bet (Rs.{MIN_BET} to Rs.{MAX_LINES}): ")
        if amount >= MIN_BET and amount<= MAX_BET:
            amount = float(amount)
        else:
            print("Enter a valid amount")
            break
    return amount

def program():
    lines = get_number_of_lines()
    balance = deposit()
    bet = get_bet()
    print(lines, balance, bet)