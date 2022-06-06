from pyfiglet import Figlet
import qrcode
import time
import os

f = Figlet(font="standard")
print(f.renderText("Amir Store"))

PRODUCT = []
listCart = []
mydict = {}
totalPrice = 0


def load():
    # time.sleep(1)
    print("Loading ...\n")

    myfile = open("database.txt", "r")
    data = myfile.read()
    products_list = data.split("\n")

    for i in range(len(products_list)):
        product_info = products_list[i].split(",")
        mydict["id"] = product_info[0]
        mydict["name"] = product_info[1]
        mydict["price"] = product_info[2]
        mydict["count"] = product_info[3]
        PRODUCT.append(mydict)
    # time.sleep(1)
    print("Welcome\n")


def add():
    for i in range(int(input("How many products do you want to add? "))):
        mydict["id"] = input("id : ")
        mydict["name"] = input("name : ")
        mydict["price"] = input("price : ")
        mydict["count"] = input("count : ")
        PRODUCT.append(mydict)


def edit():
    print(
        " 1. edit id\n",
        "2. edit name\n",
        "3. edit price\n",
        "4. edit count\n",
        "5. Cancel",
    )
    c = input("\nPlease Choose : ")

    match c:
        case "1":
            for i in range(len(PRODUCT)):
                print("ID ", [i], " : ", PRODUCT[i]["id"])
            new_ID = int(input("\nWhich ID do you want to change : "))
            PRODUCT[new_ID]["id"] = input("Enter new ID : ")
        case "2":
            for i in range(len(PRODUCT)):
                print("name ", [i], " : ", PRODUCT[i]["name"])
            new_name = int(input("\nWhich name do you want to change : "))
            PRODUCT[new_name]["name"] = input("Enter new name : ")
        case "3":
            for i in range(len(PRODUCT)):
                print("price ", [i], " : ", PRODUCT[i]["price"])
            new_price = int(input("\nWhich price do you want to change : "))
            PRODUCT[new_price]["price"] = input("Enter new price : ")
        case "4":
            for i in range(len(PRODUCT)):
                print("count ", [i], " : ", PRODUCT[i]["count"])
            new_count = int(input("\nWhich count do you want to change : "))
            PRODUCT[new_count]["count"] = input("Enter new count : ")
        case "5":
            exit()


def search():
    findFlag = 0
    findName = input("Find : ")
    for i in range(len(PRODUCT)):
        if findName == PRODUCT[i]["name"]:
            findFlag = 1
            print("Find\n", PRODUCT[i])
            break
    if findFlag == 0:
        print("Not Fond")


def show_list():
    for i in range(len(PRODUCT)):
        print(PRODUCT[i])


def delete():
    print(
        " 1. delete with id\n",
        "2. delete with name\n",
        "3. delete with price\n",
        "4. delete with count\n",
        "5. Cancel",
    )
    c = input("\nPlease Choose : ")

    match c:
        case "1":
            removeFlag = 0
            removeID = input("Enter Id")
            for i in range(len(PRODUCT)):
                if PRODUCT[i]["id"] == removeID:
                    removeFlag = 1
                    PRODUCT.remove(i)
            if removeFlag == 0:
                print("Not Find")
            else:
                print("remove successfully")
        case "2":
            removeName = 0
            removeID = input("Enter name")
            for i in range(len(PRODUCT)):
                if PRODUCT[i]["name"] == removeName:
                    removeName = 1
                    PRODUCT.remove(i)
            if removeName == 0:
                print("Not Find")
            else:
                print("remove successfully")
        case "3":
            removePrice = 0
            removeID = input("Enter price")
            for i in range(len(PRODUCT)):
                if PRODUCT[i]["price"] == removePrice:
                    removePrice = 1
                    PRODUCT.remove(i)
            if removePrice == 0:
                print("Not Find")
            else:
                print("remove successfully")
        case "4":
            removeCount = 0
            removeID = input("Enter count")
            for i in range(len(PRODUCT)):
                if PRODUCT[i]["count"] == removeCount:
                    removeCount = 1
                    PRODUCT.remove(i)
            if removeCount == 0:
                print("Not Find")
            else:
                print("remove successfully")
        case "5":
            exit()


def buy():
    while True:
        productID = input("Enter product ID : ")
        idFlag = 0
        dictCart = {}
        for i in range(len(PRODUCT)):
            if productID == PRODUCT[i]["id"]:
                idFlag = 1
                numberProducts = int(input("How many products : "))
                if numberProducts > int(PRODUCT[i]["id"]):
                    print("Inventory is not enough")
                else:
                    dictCart.update(
                        {"id": PRODUCT[i]["id"]},
                        {"name": PRODUCT[i]["name"]},
                        {"price": PRODUCT[i]["price"]},
                        {"count": PRODUCT[i]["count"]},
                    )
                    listCart.append(dictCart)
                    totalPrice += PRODUCT[i]["price"]
        if idFlag == 0:
            print("Not Fond")
        continu = input("Do you continue? y/n")
        if continu == "n":
            break
    print(listCart, "\ntotalPrice = ", totalPrice)


def QRCode():
    findFlag = 0
    findID = input("Enter ID : ")
    for i in range(len(PRODUCT)):
        if findID == PRODUCT[i]["id"]:
            data = PRODUCT[i]["id"]
            img = qrcode.make(data)
            img.save("QRCodeProduct_%i.png" % i)
            findFlag = 1
            break
    if findFlag == 0:
        print("Not Fond")


def exit():
    with open("database.txt", "a+") as f:
        f.write("\n")
        for key, value in mydict.items():
            f.write("%s," % (value))
    with open("database.txt", "a+") as f:
        for item in PRODUCT:
            f.write("%s\n" % item)
    with open("database.txt", "a+") as f:
        for item in PRODUCT:
            f.write("%s\n" % item)


def show_menu():
    # time.sleep(1)
    print(
        " 1. Add Product\n",
        "2. Edit Product\n",
        "3. Search Product\n",
        "4. Show List Product\n",
        "5. Delete Product\n",
        "6. Buy\n",
        "7. Creat QRCode\n",
        "8. Exit\n",
    )


load()
show_menu()

c = input("\nPlease Choose a Number : ")

match c:
    case "1":
        add()
    case "2":
        edit()
    case "3":
        search()
    case "4":
        show_list()
    case "5":
        delete()
    case "6":
        buy()
    case "7":
        QRCode()
    case "8":
        exit()
