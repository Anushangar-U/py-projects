MAX_LINES = 3
MAX_BET = 10000
MIN_BET = 1000

def deposit():
    while True:
        amount = input("Enter amount to deposit: ")
        if amount.isdigit():
            amount = int(amount)
            if amount > 0:
                return amount
        print("Deposit must be a positive integer greater than zero.")

def get_number_of_lines():
    while True:
        lines = input(f"Enter the number of lines (1 to {MAX_LINES}): ")
        if lines.isdigit():
            lines = int(lines)
            if 1 <= lines <= MAX_LINES:
                return lines
        print(f"Enter a valid number of lines between 1 and {MAX_LINES}.")

def get_bet():
    while True:
        amount = input(f"Enter the amount you want to bet (Rs.{MIN_BET} to Rs.{MAX_BET}): ")
        if amount.isdigit():
            amount = int(amount)
            if MIN_BET <= amount <= MAX_BET:
                return amount
        print(f"Enter a valid amount between Rs.{MIN_BET} and Rs.{MAX_BET}.")

def program():
    lines = get_number_of_lines()
    balance = deposit()
    bet = get_bet()
    total = bet * lines
    print(f"You are betting Rs.{bet} on {lines} lines. Total bet is Rs.{total}")
    if total > balance:
        print(f"Warning: your total bet (Rs.{total}) exceeds your balance (Rs.{balance}).")
    else:
        print("Bet accepted. Good luck!")
