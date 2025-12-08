import random

Player_wins = 0
Computer_wins = 0
Options = ["Scissors","Rock","Paper"]

while True:
    print("Choose your move ")
    for i, key in enumerate(Options):
        print(f"{i+1}. {key} -> {key[0]}")
    print("Enter your move : ")
    move = input().upper()

    C_move = random.choices(Options,k=1)[0]
    match move:
        case "S":
            print(f"computer's move : {C_move}")
            if C_move == "S":
                print("Draw")
            elif C_move == "P":
                print("you win")
            else:
                print("you lose")
        case "P":
            print(f"computer's move : {C_move}")
            if C_move == "P":
                print("Draw")
            elif C_move == "R":
                print("you win")
            else:
                print("you lose")
        case "R":
            print(f"computer's move : {C_move}")
            if C_move == "R":
                print("Draw")
            elif C_move == "S":
                print("you win")
            else:
                print("you lose")
        case _:
            print("Enter valid input")

    print("Do you want to continue?(y/n) :")
    decision = input().lower()
    if decision == "y":
        continue
    else:
        print("thanks for playing")
        break










