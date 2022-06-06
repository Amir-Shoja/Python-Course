import random

array = []
n = int(input("Enter size array : "))
while len(array) <= n:
    temp = random.randint(1, 100)
    if temp not in array:
        array.append(temp)
print("array : ", array)
