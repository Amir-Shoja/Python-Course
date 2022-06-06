from math import factorial

n = int(input("Number of Line : "))

for i in range(n):
    for j in range(i + 1):
        print(str(factorial(i) // (factorial(j) * factorial(i - j))).rjust(4, " "), end="  ")

    print()
