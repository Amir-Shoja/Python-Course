import time

dictionary = {}
words = []


def readFile():
    print("Loading", end="")
    time.sleep(0.5)
    print(".", end="")
    time.sleep(0.5)
    print(".", end="")
    time.sleep(0.5)
    print(".\n")
    try:
        myfile = open("WordsBank.txt", "r")
        wordList = myfile.read().split("\n")
        for i in range(0, len(wordList), 2):
            words.append({"english": wordList[i], "persian": wordList[i + 1]})

        myfile.close()
    except:
        print("An Error Occurred While Opening File!")
        exit()


def addWord():
    newKey = input("Enter new word : ")
    dictionary[newKey] = newValue = input("Enter the translation of the new word : ")
    with open("G:\\Program\\Python\\PyLearn\\Assignment_7\\WordsBank.txt", "a+") as f:
        for key, value in dictionary.items():
            f.write("%s:%s\n" % (key, value))
    words.append({"english": newKey, "persian": newValue})


def EnToPr():
    entopr = []
    sentence = input("Enter sentence :").split()
    for i in range(len(sentence)):
        # for word in words:
        if sentence[i] == words[i]["english"]:
            entopr.append(words[i]["persian"])
        else:
            entopr.append(words[i]["english"])
    print("Translate: " + " ".join(entopr))


def PrToEn():
    prtoen = []
    sentence = input("Enter sentence :").split()
    for i in range(len(sentence)):
        # for word in words:
        if sentence[i] == words[i]["persian"]:
            prtoen.append(words[i]["english"])
        else:
            prtoen.append(words[i]["persian"])
    print("Translate: " + " ".join(prtoen))


def show_menu():
    print(
        " 1. Add New Word\n",
        "2. English TO Persian\n",
        "3. Persian TO English\n",
        "4. Exit\n",
    )


readFile()
show_menu()
c = input("\nPlease Choose a Number : ")

if c == "1":
    addWord()

elif c == "2":
    EnToPr()

elif c == "3":
    PrToEn()

elif c == "4":
    exit()
