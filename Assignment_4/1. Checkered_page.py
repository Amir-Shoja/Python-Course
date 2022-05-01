def chap(n, m):
    cnt = 1
    for i in range(m):
        for j in range(n):
            if cnt % 2 == 1:
                print("#", end="")
            else:
                print("*", end="")
            cnt += 1
        cnt += 1
        print()


n = int(input("Enter n : "))
m = int(input("Enter m : "))
chap(n, m)
