import time

dictionary = {}
dictionaryEn = {}
dictionaryPr = {}
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
        myfile = open("G:\Program\Python\PyLearn\Assignment_7\WordsBank.txt", "r")
        wordList = myfile.read().split("\n")
        for i in range(len(wordList)):
            j = 0
            if i % 2 == 0:
                dictionaryEn[j] = wordList[i]
                dictionary["english"] = wordList[i]
            else:
                dictionaryPr[j] = wordList[i]
                dictionary["persian"] = wordList[i]
            words.append(dictionary)
            j += 1
            myfile.close()
    except:
        print("An Error Occurred While Opening File!")
        exit()


def addWord():
    newKey = input("Enter new word : ")
    dictionary[newKey] = newValue = input("Enter the translation of the new word : ")
    with open("G:\Program\Python\PyLearn\Assignment_7\WordsBank.txt", "a+") as f:
        for key, value in dictionary.items():
            f.write("%s:%s\n" % (key, value))
    words.append({"english": newKey, "persian": newValue})


def EnToPr():
    entopr = []
    sentence = input("Enter sentence :").split()
    for i in range(len(sentence)):
        if sentence[i] in dictionaryEn:
            for i in range(len(dictionaryEn)):
                entopr.append(dictionaryPr[i])
        else:
            print("Vocabulary is not enough")
    print("Translate: " + " ".join(sentence))


def PrToEn():
    entopr = []
    sentence = input("Enter sentence :").split()
    for i in range(len(sentence)):
        if sentence[i] in dictionaryPr:
            for i in range(len(dictionaryPr)):
                entopr.append(dictionaryEn[i])
        else:
            print("Vocabulary is not enough")
    print("Translate: " + " ".join(sentence))


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

match c:
    case "1":
        addWord()
    case "2":
        EnToPr()
    case "3":
        PrToEn()
    case "4":
        exit()
