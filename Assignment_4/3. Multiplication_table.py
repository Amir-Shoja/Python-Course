from re import L

from numpy import left_shift


def chap(n, m):
    cnt = 1
    for i in range(1, m + 1):
        for j in range(1, n + 1):
            print(str(i * j).rjust(4, " "), end="  ")
        print()


n = int(input("Enter n : "))
m = int(input("Enter m : "))
chap(n, m)
