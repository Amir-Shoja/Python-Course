n = int(input("How many student? "))
sum = max = 0
min = 100

for i in range(n):
    score = int(input("Enter score : "))
    sum += score
    if score > max:
        max = score
    if score < min:
        min = score

print("avg = ", sum / n, "\nThe highest score : ", max, "\nThe lowest score : ", min)
