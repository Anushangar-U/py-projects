import random

operators = ["+","-","*","/"]

NUM1 = random.randint(1,100)
NUM2 = random.randint(1,100)
q_opearator = random.choice(operators)

def question_generator():
    user_anws = input(f"what is {NUM1} {q_opearator} {NUM2}")
    match q_opearator:
        case "+":
            anws = NUM1 + NUM2
        case "-":
            anws = NUM1 - NUM2
        case "/":
            anws = NUM1 / NUM2
        case "*":
            anws = NUM1 * NUM2

    if user_anws == anws:
        print("correct!")
    else:
        print(f"wrong! the correct answer is {anws}")

game = input("Do you want to play a math quiz game?(y/n)").lower()

if game == "y":
    pass

elif game == "n":
    print("lets play next time.")

else:
    print("please enter a valid input.")
