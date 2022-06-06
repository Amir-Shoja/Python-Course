import random

option = ["Rock", "Paper", "Scissor"]
i = 0
score = {"user": 0, "computer": 0}
c = int(input("How many set : "))

while c > i:
    computer_choice = random.choice(option)
    user_choice = input("play game : ")
    print("\tcomputer_choice : ",computer_choice)

    if user_choice != computer_choice:
        if user_choice == "Rock" and computer_choice == "Scissor":
            score["user"] += 1
        elif user_choice == "Rock" and computer_choice == "Paper":
            score["computer"] += 1
        elif user_choice == "Paper" and computer_choice == "Scissor":
            score["computer"] += 1
        elif user_choice == "Paper" and computer_choice == "Rock":
            score["user"] += 1
        elif user_choice == "Scissor" and computer_choice == "Paper":
            score["user"] += 1
        elif user_choice == "Scissor" and computer_choice == "Rock":
            score["computer"] += 1
    else:
        computer_choice = random.choice(option)

    i += 1

if score["computer"] > score["user"]:
    print("GAME OVER\nYOU LOSS")
elif score["computer"] < score["user"]:
    print("YOU WIN")
else:
    print("DRAW")
