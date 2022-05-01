snake_length = int(input("Enter snake length : "))

for i in range(snake_length):
    if i % 2 == 1:
        print("#", end="")
    else:
        print("*", end="")
