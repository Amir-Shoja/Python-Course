from os import system, name


def show_menu():
    print(
        " 1. Addition\n",
        "2. Subtraction\n",
        "3. Convert seconds to time\n",
        "4. Convert time to seconds\n",
        "5. Exit\n",
    )


def clear():
    if name == "nt":
        _ = system("cls")
    else:
        _ = system("clear")


class time:
    def __init__(self, hour=None, minute=None, second=None):
        self.hr = hour
        self.min = minute
        self.sec = second

    def add(self, guest):
        result = time()
        result.hr = self.hr + guest.hr
        result.min = self.min + guest.min
        result.sec = self.sec + guest.sec
        if result.sec >= 60:
            result.min += 1
            result.sec -= 60
        elif result.sec >= 120:
            result.min += 2
            result.sec -= 120

        if result.min >= 60:
            result.hr += 1
            result.min -= 60
        elif result.min == 120:
            result.hr += 2
            result.min -= 120
        return result

    def sub(self, guest):
        result = time()
        result.hr = self.hr - guest.hr
        result.min = self.min - guest.min
        result.sec = self.sec - guest.sec
        if result.sec < 0:
            result.min -= 1
            result.sec += 60

        if result.min < 0:
            result.hr -= 1
            result.min += 60
        return result

    def secToTime(self):
        result = time()
        result.hr = self.sec // 3600
        result.min = (self.sec % 3600) // 60
        result.sec = (self.sec % 3600) % 60
        return result

    def timeToSec(self):
        result = self.hr * 3600 + self.min * 60 + self.sec
        return result

    def show(self):
        print(self.hr, ":", self.min, ":", self.sec)
        input()


while True:
    clear()
    show_menu()
    print("\nEnter Time\n")
    fristTime = time(
        int(input("hour 1 : ")), int(input("minute 1 : ")), int(input("second 1 : "))
    )
    secondTime = time(
        int(input("hour 2 : ")), int(input("minute 2 : ")), int(input("second 2 : "))
    )

    c = input("\nPlease Choose a Number of menus : ")

    match c:
        case "1":
            a = fristTime.add(secondTime)
            a.show()
        case "2":
            m = fristTime.sub(secondTime)
            m.show()
        case "3":
            s = fristTime.secToTime(secondTime)
            s.show()
        case "4":
            d = fristTime.timeToSec(secondTime)
            d.show()
        case "5":
            exit()
