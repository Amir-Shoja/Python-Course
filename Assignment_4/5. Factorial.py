from math import factorial

number = int(input("Enter Number : "))
cnt = flag = 0

while factorial(cnt) <= number:
    if factorial(cnt) == number:
        flag = 1
    cnt += 1

if flag == 1:
    print("YES")
else:
    print("NO")
