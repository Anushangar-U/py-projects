with open("story.txt", "r") as file:
    story = file.read()

words = []
start_of_word = -1

for i,char in enumerate(story):
    if char == "<":
        start_of_word = i

    if char == ">" and start_of_word != -1:
        word = story[start_of_word: i]
        words.append(word)
        start_of_word = -1

print(words)
