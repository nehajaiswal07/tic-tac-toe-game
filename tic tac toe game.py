# x  0  x
# 0  x  0
# x  0  x
# import math
# import random

#computer
# player="x"
# space=random.SystemRandom()

import random

def tic_toe():
    choose=print("Lets start!,Choose any one-X,0")
    player=input("what you want!")
    computer=''
    
    if player=='X':
        computer='0'
    else:
        computer='X'
        
    # board1=print(f"{1}._         {2}._       {3}._\n")
    # board2=print(f"{4}._         {5}._        {6}._\n")
    # board3=print(f"{7}._         {8}._        {9}._\n")
    
    board=["__","__ ","__ ",
           "__ ","__ ","__ ",
           "__ ","__ ","__ "]
    print(eval(board))
    player_chance=int(input("choose place you want to enter!\n"))
    computer_chance=random.randint(1,9)
    if player_chance==board[0]:
       print('X', board)


tic_toe()

    # ----------------------------------------
# import random
# def intro():
#     print("Welcome to tic tac toe game!\n")
#     input=print("press enter to continue!\n")
# intro()

# def board():
#     print("here is your board")
#     board=[[" "," "," "],
#            [" "," "," "],
#            [" "," "," "]]
#     return board

# def play_game():
#     pass

    
