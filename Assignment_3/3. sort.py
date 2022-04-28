n = int(input("Enter size list : "))
lst_1 = []

for i in range(n):
    temp = float(input())
    lst_1.append(temp)
lst_2 = sorted(lst_1)

print(lst_2 == lst_1)
