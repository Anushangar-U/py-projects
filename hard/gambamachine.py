import random

MAX_LINES = 3
MAX_BET = 10000
MIN_BET = 1000

ROWS = 3
COLS = 3

s_count = {"A": 2, "B": 3, "C": 4, "D": 5}
s_values = {"A": 5, "B": 4, "C": 3, "D": 2}

def slot_spin():
    symbol_collections = []
    for symbol, count in s_count.items():
        for i in range(count):
            symbol_collections.append(symbol)

    columns = []
    for i in range(COLS):
        column = []
        for j in range(ROWS):
            value = random.choice(symbol_collections)
            column.append(value)
        columns.append(column) 
    return columns

def get_SlotMchn(columns):
    for row in range(len(columns[0])):
        for i, column in enumerate(columns):
            if i != len(columns) - 1:
                print(f"{column[row]} | ", end="")
            else:
                print(f"{column[row]}")

def check_winnings(columns, lines, bet, values):
    winnings = 0
    for line in range(lines):
        symbol = columns[0][line]
        for column in columns:
            symbol_to_check = column[line]
            if symbol != symbol_to_check:
                break
        else:
            winnings += values[symbol] * bet
    return winnings

def deposit():
    while True:
        amount = input("Enter amount to deposit: Rs.")
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
        amount = input(f"Enter the amount you want to bet per line (Rs.{MIN_BET} to Rs.{MAX_BET}): ")
        if amount.isdigit():
            amount = int(amount)
            if MIN_BET <= amount <= MAX_BET:
                return amount
        print(f"Enter a valid amount between Rs.{MIN_BET} and Rs.{MAX_BET}.")

def program():
    balance = deposit()
    
    while True:
        print(f"\nCurrent balance: Rs.{balance}")
        spin_choice = input("Press enter to play (q to quit): ")
        if spin_choice.lower() == "q":
            break
            
        lines = get_number_of_lines()
        
        while True:
            bet = get_bet()
            total = bet * lines
            if total > balance:
                print(f"You do not have enough to bet that amount, your current balance is: Rs.{balance}")
            else:
                break
                
        print(f"You are betting Rs.{bet} on {lines} lines. Total bet is Rs.{total}")
        balance -= total
        
        slots = slot_spin()
        get_SlotMchn(slots)
        
        winnings = check_winnings(slots, lines, bet, s_values)
        balance += winnings
        
        print(f"You won Rs.{winnings}.")