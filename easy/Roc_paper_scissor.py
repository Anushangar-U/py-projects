import random

player_wins = 0
computer_wins = 0
options = ["Scissors", "Rock", "Paper"]

while True:
    print("\n--------------------------------")
    print(f"SCORE -> You: {player_wins} | Computer: {computer_wins}")
    print("--------------------------------")
    
    print("Choose your move:")
    for i, key in enumerate(options):
        print(f"{i+1}. {key} -> {key[0]}")
        
    print("Enter your move (S, P, R): ")
    move = input().upper()

    if move not in ["S", "P", "R"]:
        print("Invalid input. Please type S, P, or R.")
        continue

    pc_full_word = random.choice(options) 
    pc_letter = pc_full_word[0]

    print(f"Computer chose: {pc_full_word}")

    if move == pc_letter:
        print("Result: Draw")
    
    elif (move == "S" and pc_letter == "P") or \
         (move == "P" and pc_letter == "R") or \
         (move == "R" and pc_letter == "S"):
        print("Result: You Win")
        player_wins += 1
    
    else:
        print("Result: You Lose")
        computer_wins += 1

    decision = input("Do you want to continue? (y/n): ").lower()
    if decision != "y":
        print(f"Final Score -> You: {player_wins} | Computer: {computer_wins}")
        print("Thanks for playing.")
        break