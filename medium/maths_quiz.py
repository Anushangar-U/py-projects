import random
import time

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

    print("You have 10 seconds to answer!")

    start_time = time.time()

    try:
        user_ans = float(input("Your answer: "))
        
        end_time = time.time()
        time_taken = end_time - start_time
        
        if time_taken > 10:
            print(f"Too slow! You took {round(time_taken, 1)} seconds.")
        else:
            if user_ans == ans:
                print(f"Correct! You answered in {round(time_taken, 1)} seconds.")
            else:
                print(f"Wrong! The correct answer is {ans}")
            
    except ValueError:
        print("Invalid input. Please enter a number next time.")

print("---- Welcome to the Math Quiz ----")

while True:
    game = input("\nDo you want to play a math quiz game? (y/n): ").strip().lower()

    if game == "y":
        question_generator()
    elif game == "n":
        print("Let's play next time.")
        break
    else:
        print("Please enter 'y' for yes or 'n' for no.")