from cmath import sqrt


def quadraticEquation(a, b, c):
    delta = b * b - 4 * a * c
    sqrt_val = sqrt(abs(delta))

    if delta > 0:
        print("2 Answers :\n")
        print("X1 = ", (-b + sqrt_val) / (2 * a))
        print("X2 = ", (-b - sqrt_val) / (2 * a))

    elif delta == 0:
        print("1 Answers : \n")
        print(-b / (2 * a))

    else:
        print("Complex Roots")
        print(-b / (2 * a), " + i", sqrt_val)
        print(-b / (2 * a), " - i", sqrt_val)


a = float(input("Enter a : "))
b = float(input("Enter b : "))
c = float(input("Enter c : "))

if a == 0:
    print("Input correct quadratic equation")

else:
    quadraticEquation(a, b, c)
