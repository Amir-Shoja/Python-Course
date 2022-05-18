from os import system, name


def clear():
    if name == "nt":
        _ = system("cls")

    else:
        _ = system("clear")


def show_menu():
    print(
        " 1. Addition\n",
        "2. multiplied\n",
        "3. Subtraction\n",
        "5. Exit\n",
    )


def show(x):
    print(x["a"], "+", "i", x["b"])
    input("\nplease enter key to continue...")


def Addition(a, b):
    addCom = {}
    addCom["a"] = a["a"] + b["a"]
    addCom["b"] = a["b"] + b["b"]
    show(addCom)


def Subtraction(a, b):
    subCom = {}
    subCom["a"] = a["a"] - b["a"]
    subCom["b"] = a["b"] - b["b"]
    show(subCom)


def multiplied(a, b):
    mulCom = {}
    mulCom["a"] = a["a"] * b["a"] - b["b"] * b["b"]
    mulCom["b"] = a["a"] * b["b"] + b["a"] * a["b"]

    show(mulCom)


while True:
    clear()
    show_menu()
    complex_1 = {}
    complex_2 = {}
    print("complex number = a + ib", end="\n")
    print("\nfirst complex number\n")
    complex_1["a"] = int(input("enter a : "))
    complex_1["b"] = int(input("enter b : "))
    print("\nsecond complex number\n")
    complex_2["a"] = int(input("enter a : "))
    complex_2["b"] = int(input("enter b : "))

    c = input("\nPlease Choose a Number : ")
    match c:
        case "1":
            Addition(complex_1, complex_2)
        case "2":
            multiplied(complex_1, complex_2)
        case "3":
            Subtraction(complex_1, complex_2)
        case "4":
            exit()
