with open("story.txt", "r") as file:
    story = file.read()

words = set()
start_of_word = -1

for i,char in enumerate(story):
    if char == "<":
        start_of_word = i

    if char == ">" and start_of_word != -1:
        word = story[start_of_word: i + 1]
        words.add(word)
        start_of_word = -1

anwers = {}

for word in words:
    user_input = input(f"Enter a {word}: ")
    anwers[word] = user_input

for word, user_input in anwers.items():
    story = story.replace(word, user_input)

print("\nHere is your story:\n")
print(story)
