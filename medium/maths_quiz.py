import random

def question_generator():
    operators = ["+", "-", "*", "/"]

    num1 = random.randint(1, 100)
    num2 = random.randint(1, 100)
    q_operator = random.choice(operators)

    match q_operator:
        case "+":
            ans = num1 + num2
        case "-":
            ans = num1 - num2
        case "/":
            ans = round(num1 / num2, 2)
        case "*":
            ans = num1 * num2

    if q_operator == "/":
        print(f"What is {num1} {q_operator} {num2}? (Round to 2 decimal places)")
    else:
        print(f"What is {num1} {q_operator} {num2}?")

    try:
        user_ans = float(input("Your answer: "))
        if user_ans == ans:
            print("Correct! Good job.")
        else:
            print(f"Wrong! The correct answer is {ans}")
            
    except ValueError:
        print("Invalid input. Please enter a number next time.")

print("--- Welcome to the Math Quiz ---")

while True:
    game = input("\nDo you want to play a math quiz game? (y/n): ").strip().lower()

    if game == "y":
        question_generator()
    elif game == "n":
        print("Let's play next time. Bye!")
        break
    else:
        print("Please enter 'y' for yes or 'n' for no.")