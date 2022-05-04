import sys
from termcolor import colored, cprint
from colorama import Fore, Style
from random import randrange
import time

start_time = time.time()

cnt = 0
flag_winer = 0
board = [["_", "_", "_"], ["_", "_", "_"], ["_", "_", "_"]]


def timer():
    print("\n\t %s seconds" % (time.time() - start_time))


def chap():
    for i in range(3):
        for j in range(3):
            if board[i][j] == "X":
                print(Fore.RED + "X", end=" ")
                print(Style.RESET_ALL, end="")
            elif board[i][j] == "O":
                print(Fore.CYAN + "O", end=" ")
                print(Style.RESET_ALL, end="")
            else:
                print(board[i][j], end=" ")
        print()


def check_win():
    # ROWs
    if board[0][0] == "X" and board[0][1] == "X" and board[0][2] == "X":
        print("First player Winner !!!!")
        chap()
        timer()
        exit()
    elif board[1][0] == "X" and board[1][1] == "X" and board[1][2] == "X":
        print("First player Winner !!!!")
        chap()
        timer()
        exit()
    elif board[2][0] == "X" and board[2][1] == "X" and board[2][2] == "X":
        print("First player Winner !!!!")
        chap()
        timer()
        exit()
    # COLs
    elif board[0][0] == "X" and board[1][0] == "X" and board[2][0] == "X":
        print("First player Winner !!!!")
        chap()
        timer()
        exit()
    elif board[0][1] == "X" and board[1][1] == "X" and board[2][1] == "X":
        print("First player Winner !!!!")
        chap()
        timer()
        exit()
    elif board[0][2] == "X" and board[1][2] == "X" and board[2][2] == "X":
        print("First player Winner !!!!")
        chap()
        timer()
        exit()
    # Diameter
    elif board[0][0] == "X" and board[1][1] == "X" and board[2][2] == "X":
        print("First player Winner !!!!")
        chap()
        timer()
        exit()
    elif board[0][2] == "X" and board[1][1] == "X" and board[2][0] == "X":
        print("First player Winner !!!!")
        chap()
        timer()
        exit()
    # ROWs
    elif board[0][0] == "O" and board[0][1] == "O" and board[0][2] == "O":
        print("Second player Winner !!!!")
        chap()
        timer()
        exit()
    elif board[1][0] == "O" and board[1][1] == "O" and board[1][2] == "O":
        print("Second player Winner !!!!")
        chap()
        timer()
        exit()
    elif board[2][0] == "O" and board[2][1] == "O" and board[2][2] == "O":
        print("Second player Winner !!!!")
        chap()
        timer()
        exit()
    # COLs
    elif board[0][0] == "O" and board[1][0] == "O" and board[2][0] == "O":
        print("Second player Winner !!!!")
        chap()
        timer()
        exit()
    elif board[0][1] == "O" and board[1][1] == "O" and board[2][1] == "O":
        print("Second player Winner !!!!")
        chap()
        timer()
        exit()
    elif board[0][2] == "O" and board[1][2] == "O" and board[2][2] == "O":
        print("Second player Winner !!!!")
        chap()
        timer()
        exit()
    # Diameter
    elif board[0][0] == "O" and board[1][1] == "O" and board[2][2] == "O":
        print("Second player Winner !!!!")
        chap()
        timer()
        exit()
    elif board[0][0] == "X" and board[1][1] == "X" and board[2][2] == "X":
        print("Second player Winner !!!!")
        chap()
        timer()
        exit()
    elif board[0][2] == "X" and board[1][1] == "X" and board[2][0] == "X":
        print("Second player Winner !!!!")
        chap()
        timer()
        exit()
    elif board[0][2] == "O" and board[1][1] == "O" and board[2][0] == "O":
        print("Second player Winner !!!!")
        chap()
        timer()
        exit()
    elif cnt > 7:
        print("DRAW")


def input_player_one():
    cprint("\nFirst player", "red", attrs=["reverse", "blink"])
    row = int(input("\nEnter ROW : "))
    col = int(input("Enter COL : "))
    if board[row][col] != "O" and board[row][col] != "X":
        board[row][col] = "X"
    else:
        print("\n\tYou should not put the nut here\n\ttry again")
        input_player_one()


def input_player_tow():
    cprint("\nSecond player", "blue", attrs=["reverse", "blink"])
    row = int(input("\nEnter ROW : "))
    col = int(input("Enter COL : "))
    if board[row][col] != "O" and board[row][col] != "X":
        board[row][col] = "O"
    else:
        print("\n\tYou should not put the nut here\n\ttry again")
        input_player_tow()


def input_computer_player():
    cprint("\ncomputer player", "blue", attrs=["reverse", "blink"])
    while True:
        row = randrange(0, 3)
        col = randrange(0, 3)
        if board[row][col] != "O" and board[row][col] != "X":
            board[row][col] = "O"
            break


print("MENU\n1. on Player\n2. tow player\n3. Quit")
c = input()
match c:
    case "1":
        while True:
            chap()
            input_player_one()
            check_win()
            chap()
            input_computer_player()
            check_win()
            cnt + 1
    case "2":
        while True:
            chap()
            input_player_one()
            check_win()
            chap()
            input_player_tow()
            check_win()
            cnt + 1
    case "3":
        exit()
