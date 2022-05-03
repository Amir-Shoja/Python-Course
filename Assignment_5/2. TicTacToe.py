import sys
from termcolor import colored, cprint

flag_winer = 0
board = [["_", "_", "_"], ["_", "_", "_"], ["_", "_", "_"]]


def chap():
    for i in range(3):
        for j in range(3):
            print(board[i][j], end=" ")
        print()


def check_win():
    # ROWs
    if board[0][0] == "X" and board[0][1] == "X" and board[0][2] == "X":
        print("First player Winner !!!!")
        exit()
    elif board[1][0] == "X" and board[1][1] == "X" and board[1][2] == "X":
        print("First player Winner !!!!")
        exit()
    elif board[2][0] == "X" and board[2][1] == "X" and board[2][2] == "X":
        print("First player Winner !!!!")
        exit()
    # COLs
    elif board[0][0] == "X" and board[1][0] == "X" and board[2][0] == "X":
        print("First player Winner !!!!")
        exit()
    elif board[0][1] == "X" and board[1][1] == "X" and board[2][1] == "X":
        print("First player Winner !!!!")
        exit()
    elif board[0][2] == "X" and board[1][2] == "X" and board[2][2] == "X":
        print("First player Winner !!!!")
        exit()
    # Diameter
    elif board[0][0] == "X" and board[1][1] == "X" and board[2][2] == "X":
        print("First player Winner !!!!")
        exit()
    elif board[0][2] == "X" and board[1][1] == "X" and board[2][0] == "X":
        print("First player Winner !!!!")
        exit()
    # ROWs
    elif board[0][0] == "O" and board[0][1] == "O" and board[0][2] == "O":
        print("Second player Winner !!!!")
        exit()
    elif board[1][0] == "O" and board[1][1] == "O" and board[1][2] == "O":
        print("Second player Winner !!!!")
        exit()
    elif board[2][0] == "O" and board[2][1] == "O" and board[2][2] == "O":
        print("Second player Winner !!!!")
        exit()
    # COLs
    elif board[0][0] == "O" and board[1][0] == "O" and board[2][0] == "O":
        print("Second player Winner !!!!")
        exit()
    elif board[0][1] == "O" and board[1][1] == "O" and board[2][1] == "O":
        print("Second player Winner !!!!")
        exit()
    elif board[0][2] == "O" and board[1][2] == "O" and board[2][2] == "O":
        print("Second player Winner !!!!")
        exit()
    # Diameter
    elif board[0][0] == "O" and board[1][1] == "O" and board[2][2] == "O":
        print("Second player Winner !!!!")
        exit()
    elif board[0][2] == "X" and board[1][1] == "X" and board[2][0] == "X":
        print("Second player Winner !!!!")
        exit()
    else:
        print("DRAW")


def input_player_one():
    cprint("\nFirst player", "red", attrs=["reverse", "blink"])
    row = int(input("\nEnter ROW : "))
    col = int(input("Enter COL : "))
    board[row][col] = "X"


def input_player_tow():
    cprint("\nSecond player", "blue", attrs=["reverse", "blink"])
    row = int(input("\nEnter ROW : "))
    col = int(input("Enter COL : "))
    board[row][col] = "O"


while True:
    chap()
    input_player_one()
    check_win()
    chap()
    input_player_tow()
    check_win()
