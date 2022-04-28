import random

words = [
    "book",
    "tree",
    "python",
    "bag",
    "umbrella",
    "dog",
    "clock",
    "engineer",
    "toothpaste",
    "shirmoz",
]

word = random.choice(words)  # clock
gauss = word.capitalize()
joon = 10
cnt = 0
answer = []

print("- " * len(word))  # - - - - -

while joon > 0:
    user_character = input()  # s

    if user_character in word or user_character in gauss:
        cnt += 1
        print("yes")
        answer.append(user_character)
        if cnt == len(word):
            break
    else:
        joon = joon - 1
        print("no")

for i in range(len(word)):
    print(answer[i], end="")
