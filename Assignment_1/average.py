name = input("Enter You'r name : ")
family = input("Enter You'r family : ")
score_1 = float(input("score_1 : "))
score_2 = float(input("score_2 : "))
score_3 = float(input("score_3 : "))

avg = (score_1 + score_2 + score_3) / 3

if avg >= 17:
    print("Great")
elif avg < 17 and avg >= 12:
    print("Normal ")
else:
    print("Fail ")
