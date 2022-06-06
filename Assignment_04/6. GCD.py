def gcd(a, b):
    if b == 0:
        return a
    return gcd(b, a % b)


a = int(input("Enter num1 : "))
b = int(input("Enter num2 : "))

print("gcd = ", gcd(a, b))
