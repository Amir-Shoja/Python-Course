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
    myFile = open("translate.txt", "a")
    newEnWord = input("Enter new english word : ")
    newPrWord = input("Enter the translation of the new word : ")
    myFile.write("\n%s\n%s" % (newEnWord, newPrWord))
    myFile.close()
    words.append({"english": newEnWord, "persian": newPrWord})


def EnToPr():
    entopr = []
    sentence = input("Enter sentence :").split()
    for i in range(len(sentence)):
        for j in range(len(words)):
            if sentence[i] == words[j]["english"]:
                entopr.append(words[j]["persian"])
            else:
                entopr.append(words[i]["english"])
    print("Translate: " + " ".join(entopr))


def PrToEn():
    prtoen = []
    sentence = input("Enter sentence :").split()
    for i in range(len(sentence)):
        for j in range(len(words)):
            if sentence[i] == words[j]["persian"]:
                prtoen.append(words[j]["english"])
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
