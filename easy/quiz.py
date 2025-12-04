print("Welcome to the quiz!")

game = input("Do you want to start? (y/n) : ")

if game.lower() == 'y':
    print("Choose the topic for your quiz")
    quiz_topic = ["Computer", "Animals", "Birds", "Humans"]
    
    for i, topic in enumerate(quiz_topic):
        print(f"{i+1}. {topic} -> {topic[0]}") 

    print("\nEnter the first letter of the desired quiz (Eg: Computer -> C) :")
    Selected_quiz = input().lower()

    score = 0
    final_user_answers = []
    final_correct_answers = []

    match Selected_quiz:
        case "c":
            print("\n--- COMPUTER QUIZ ---")
            Computer_anws = []
            Computer_crt_anws = ["ROM", "DisplayPort", "PCIe", "SRAM", "NVMe"]

            Computer_anws.append(input("What component stores the BIOS/UEFI? "))
            Computer_anws.append(input("Which port is commonly used for monitors today (after HDMI)? "))
            Computer_anws.append(input("Which connector supplies power to the GPU? "))
            Computer_anws.append(input("What type of memory is used as CPU cache? "))
            Computer_anws.append(input("What type of SSD uses the M.2 slot with maximum speed? "))

            final_user_answers = Computer_anws
            final_correct_answers = Computer_crt_anws

        case "a":
            print("\n--- ANIMAL QUIZ ---")
            Animal_anws = []
            Animal_crt_anws = ["Cheetah", "Blue Whale", "Camel", "Bat", "8"]

            Animal_anws.append(input("Which is the fastest land animal? "))
            Animal_anws.append(input("Which is the largest mammal in the world? "))
            Animal_anws.append(input("Which animal is known as the 'Ship of the Desert'? "))
            Animal_anws.append(input("What is the only mammal that can fly? "))
            Animal_anws.append(input("How many legs does a spider have? "))

            final_user_answers = Animal_anws
            final_correct_answers = Animal_crt_anws

        case "b":
            print("\n--- BIRD QUIZ ---")
            Bird_anws = []
            Bird_crt_anws = ["Dove", "Penguin", "Ostrich", "Owl", "Ostrich"]

            Bird_anws.append(input("Which bird is the universal symbol of peace? "))
            Bird_anws.append(input("Which bird cannot fly but swims in ice? "))
            Bird_anws.append(input("Which is the largest bird in the world? "))
            Bird_anws.append(input("Which bird can rotate its head 270 degrees? "))
            Bird_anws.append(input("Which bird lays the largest egg? "))

            final_user_answers = Bird_anws
            final_correct_answers = Bird_crt_anws

        case "h":
            print("\n--- HUMAN BODY QUIZ ---")
            Human_anws = []
            Human_crt_anws = ["206", "Skin", "Heart", "Enamel", "4"]

            Human_anws.append(input("How many bones are in the adult human body? "))
            Human_anws.append(input("What is the largest organ in the human body? "))
            Human_anws.append(input("Which organ pumps blood throughout the body? "))
            Human_anws.append(input("What is the hardest substance in the human body? "))
            Human_anws.append(input("How many chambers does the human heart have? "))

            final_user_answers = Human_anws
            final_correct_answers = Human_crt_anws

        case _:
            print("Invalid Choice! Please restart and select C, A, B, or H.")

    if len(final_user_answers) > 0:
        print("\n--- RESULTS ---")
        for u_ans, c_ans in zip(final_user_answers, final_correct_answers):
            if u_ans.lower() == c_ans.lower():
                print(f"Correct! ({c_ans})")
                score += 1
            else:
                print(f"Wrong! You said '{u_ans}', but the answer was '{c_ans}'")

        print(f"\nFINAL SCORE: {score}/5")

else:
    print("Okay, maybe next time!")