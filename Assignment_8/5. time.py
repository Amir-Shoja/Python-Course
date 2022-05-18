from os import system, name


def clear():
    if name == "nt":
        _ = system("cls")
    else:
        _ = system("clear")


def show(x):
    print(x["hour"], ":", x["minute"], ":", x["second"])
    input("\nplease enter key to continue ")


def show_menu():
    print(
        " 1. Addition\n",
        "2. Subtraction\n",
        "3. Convert seconds to time\n",
        "4. Convert time to seconds\n",
        "5. Exit\n",
    )


def Addition(t1, t2):
    time = {}
    time["hour"] = t1["h"] + t2["h"]
    time["minute"] = t1["m"] + t2["m"]
    time["second"] = t1["s"] + t2["s"]

    if time["second"] >= 60:
        time["second"] -= 60
        time["minute"] += 1
    elif time["second"] == 120:
        time["second"] -= 120
        time["minute"] += 2

    if time["minute"] >= 60:
        time["minute"] -= 60
        time["hour"] += 1
    elif time["minute"] == 120:
        time["minute"] -= 120
        time["hour"] += 2
    show(time)


def Subtraction(t1, t2):
    time = {}
    time["second"] = t1["s"] - t2["s"]
    time["minute"] = t1["m"] - t2["m"]
    time["hour"] = t1["h"] - t2["h"]
    if time["second"] < 0:
        time["minute"] -= 1
        time["second"] += 60
    if time["minute"] < 0:
        time["hour"] -= 1
        time["minute"] += 60
    show(time)


def secToTime(sectime):
    secTime = {}
    secTime["hour"] = sectime // 3600
    secTime["minute"] = (sectime % 3600) // 60
    secTime["second"] = (sectime % 3600) % 60
    show(secTime)


def timeToSec(timesec):
    sec = (((timesec["hour"] * 60) + timesec["minute"]) * 60) + timesec["second"]
    print("seconds = ", sec)
    input("\nplease enter key to continue ")


while True:
    clear()
    show_menu()
    c = input("\nPlease Choose a Number : ")

    match c:
        case "1":
            print("\nEnter the clock 1\n")
            time1 = {
                "h": int(input("Enter hour : ")),
                "m": int(input("Enter minute : ")),
                "s": int(input("Enter second : ")),
            }
            print("\nEnter the clock 2\n")
            time2 = {
                "h": int(input("Enter hour : ")),
                "m": int(input("Enter minute : ")),
                "s": int(input("Enter second : ")),
            }
            Addition(time1, time2)

        case "2":
            print("\nEnter the clock 1\n")
            time1 = {
                "h": int(input("Enter hour : ")),
                "m": int(input("Enter minute : ")),
                "s": int(input("Enter second : ")),
            }
            print("\nEnter the clock 2\n")
            time2 = {
                "h": int(input("Enter hour : ")),
                "m": int(input("Enter minute : ")),
                "s": int(input("Enter second : ")),
            }
            Subtraction(time1, time2)

        case "3":
            sectime = int(input("Enter Time : "))
            secToTime(sectime)

        case "4":
            timesec = {
                "hour": int(input("Enter hour : ")),
                "minute": int(input("Enter minute : ")),
                "second": int(input("Enter second : ")),
            }

            timeToSec(timesec)
        case "5":
            exit()
