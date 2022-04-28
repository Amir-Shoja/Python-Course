fib = []
n = int(input("How many numbers should be added?"))

for i in range(n):
    if i < 2:
        fib.append(1)
    else:
        fib.append(fib[i - 1] + fib[i - 2])

print(fib)
