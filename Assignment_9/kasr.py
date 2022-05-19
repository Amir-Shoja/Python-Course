from os import system, name


def show_menu():
    print(" 1. add\n", "2. multiplied\n", "3. subtract\n", "4. divide\n", "5. Exit\n")


def clear():
    if name == "nt":
        _ = system("cls")
    else:
        _ = system("clear")


class kasr:
    def __init__(self, Numerator, Denominator):
        self.soorat = Numerator
        self.makhraj = Denominator

    def sum(self, guest):
        result = kasr(None, None)
        result.soorat = self.makhraj * guest.soorat + self.soorat * guest.makhraj
        result.makhraj = self.makhraj * guest.makhraj
        return result

    def mul(self, guest):
        result = kasr(None, None)
        result.soorat = self.soorat * guest.soorat
        result.makhraj = self.makhraj * guest.makhraj
        return result

    def sub(self, guest):
        result = kasr(None, None)
        result.soorat = self.soorat * guest.makhraj - guest.soorat * self.makhraj
        result.makhraj = self.makhraj * guest.makhraj
        return result

    def div(self, guest):
        result = kasr(None, None)
        result.soorat = self.soorat * guest.makhraj
        result.makhraj = self.makhraj * guest.soorat
        return result

    def show(self):
        print(self.soorat, "/", self.makhraj)
        input()


while True:
    clear()
    show_menu()
    print("\nEnter Numerator and Denominator of fractions\n")
    fristKasr = kasr(float(input("Numerator 1 : ")), float(input("Denominator 1 : ")))
    secondKasr = kasr(float(input("Numerator 2 : ")), float(input("Denominator 2 : ")))

    c = input("\nPlease Choose a Number : ")

    match c:
        case "1":
            a = fristKasr.sum(secondKasr)
            a.show()
        case "2":
            m = fristKasr.mul(secondKasr)
            m.show()
        case "3":
            s = fristKasr.sub(secondKasr)
            s.show()
        case "4":
            d = fristKasr.div(secondKasr)
            d.show()
        case "5":
            exit()
