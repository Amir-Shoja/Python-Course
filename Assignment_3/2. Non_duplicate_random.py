import random

array = []
n = int(input("Enter size array : "))

for i in range(n):
    temp = random.randint(1, 100)
    if temp not in array:
        array.append(temp)

print("array : ", array)
