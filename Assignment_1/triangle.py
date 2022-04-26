print("Enter the size of the triangle side: ")
a = float(input("a : "))
b = float(input("b : "))
c = float(input("c : "))

if a < b + c and b < a + c and c < a + b:
    print("Yes, we have triangle.")
    if a == b and b == c:
        print("EQUILATERAL TRIANGLE")
    elif a == b or a == c or b == c:
        print("ISOSCELES TRIANGLE")
    elif a == b and b == c:
        print("EQUILATERAL TRIANGLE")
    elif (
        a**2 == b**2 + c**2
        or b**2 == a**2 + c**2
        or c**2 == a**2 + b**2
    ):
        print("RIGHT ANGLED TRIANGLE")

else:
    print("No, we Don't have triangle.")
