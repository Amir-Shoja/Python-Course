from os import system, name


def show_menu():
    print(" 1. add\n", "2. multiplied\n", "3. subtract\n", "4. divide\n", "5. Exit\n")


def show(x):
    print(x["Numerator"], "/", x["Denominator"])
    input()


def clear():
    if name == "nt":
        _ = system("cls")
    else:
        _ = system("clear")


def add(frac1, frac2):
    result = {}
    result["Numerator"] = (
        frac1["Numerator"] * frac2["Denominator"]
        + frac2["Numerator"] * frac1["Denominator"]
    )
    result["Denominator"] = frac1["Denominator"] * frac2["Denominator"]
    show(result)


def multiplied(frac1, frac2):
    result = {}
    result["Numerator"] = frac1["Numerator"] * frac2["Numerator"]
    result["Denominator"] = frac1["Denominator"] * frac2["Denominator"]
    show(result)


def subtract(frac1, frac2):
    result = {}
    result["Numerator"] = (
        frac1["Numerator"] * frac2["Denominator"]
        - frac2["Numerator"] * frac1["Denominator"]
    )
    result["Denominator"] = frac1["Denominator"] * frac2["Denominator"]
    show(result)


def divide(frac1, frac2):
    result = {}
    result["Numerator"] = frac1["Numerator"] * frac2["Denominator"]
    result["Denominator"] = frac1["Denominator"] * frac2["Numerator"]
    show(result)


while True:
    clear()
    show_menu()
    print("\nEnter Numerator and Denominator of fractions\n")
    firstFraction = {
        "Numerator": float(input("Numerator 1 : ")),
        "Denominator": float(input("Denominator 1 : ")),
    }
    secondFraction = {
        "Numerator": float(input("Numerator 2 : ")),
        "Denominator": float(input("Denominator 2 : ")),
    }
    c = input("\nPlease Choose a Number : ")

    match c:
        case "1":
            add(firstFraction, secondFraction)
        case "2":
            multiplied(firstFraction, secondFraction)
        case "3":
            subtract(firstFraction, secondFraction)
        case "4":
            divide(firstFraction, secondFraction)
        case "5":
            exit()
