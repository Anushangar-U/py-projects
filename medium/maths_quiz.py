import random

operators = ["+","-","*","/"]

NUM1 = random.randint(1,100)
NUM2 = random.randint(1,100)

def logic():
    pass

game = input("Do you want to play a math quiz game?(y/n)").lower()

if game == "y":
    pass

elif game == "n":
    print("lets play next time.")

else:
    print("please enter a valid input.")
