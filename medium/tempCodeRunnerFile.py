import random

play = input("Do you want to play the game?(y/n) : ").lower()

Total_score = 0

def dice_score():
    result = random.randint(1, 6)
    return result

if play == "y":
    print("===================Rules====================")
    print("1.If you roll 1 your score will set to 0 and your turn ends.")
    print("2.As long as you didn't roll 1 you can continue infinitely or press ""n"" to end turn early can keep your score.")
    print("3.Pressing ""y"" will allow to continue to roll dice until you hit 0.")
    print()

    while True:
        choice = input("Roll dice?(y/n) : ").lower()
        match choice:
            case "y":
                if dice_score() == 1:
                    print(f"Your last dice roll : {dice_score()} !!! oops unclucky")
                    print(f"Your Total Score is 0")
                    break
                else:
                    Total_score = Total_score + dice_score()
                    print(f"Your last dice roll : {dice_score()}")
                    print(f"Current score : {Total_score}")
            case "n":
                print(f"Your final score is {Total_score}")
                break
                
elif play == "n":
    print("Let's play latter !")

else:
    print("Invlaid input please enter y/n !!!")