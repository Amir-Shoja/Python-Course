import random

n = random.randrange(1, 7)

while True:
    print(n)
    if n == 6:
        print("You won!!!")
        n = random.randrange(1, 7)
    else:
        break
