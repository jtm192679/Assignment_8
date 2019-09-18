print("welcome to the game")                           #tic tac toe game
list1 = [1, 3, 5, 7, 9]
list2 = [2, 4, 6, 8]
board = [0, 0, 0, 0, 0, 0, 0, 0, 0]
print(board[0], board[1], board[2])                     #showing blank tic tac toe to players
print(board[2], board[3], board[4])
print(board[6], board[7], board[8])
while [True]:
    n = int(input("press 1 for player1's chance  and press 2 for player2's chance:"))     #giving options to players
    if (n == 1):
        print("player1's chgance")
        p1 = list1

        a = int(input("enter the position:"))                                  #taking position and value from player1
        b = int(input("enter the number to be entered from list1:"))
        print("postion and number to be entered: %d %d " % (a, b))

        board[a - 1] = b
        print(board)
        print(board[0], board[1], board[2])
        print(board[3], board[4], board[5])
        print(board[6], board[7], board[8])                                    #checking sum to declare winner

        i = board[0] + board[1] + board[2]
        j = board[3] + board[4] + board[5]
        k = board[6] + board[7] + board[8]
        m = board[0] + board[3] + board[8]
        n = board[2] + board[3] + board[6]
    if(i==15):
        print ("player1 is winner")
    elif(j==15):
        print ("player1 is winner")
    elif(k==15):
        print ("player1 is winner")
    elif(m==15):
        print ("player1 is winner")
    elif(n==15):
        print ("player1 is winner")
    p = int(input("press 2 for player2's chance:"))                    #option for player2
    if (p == 2):
        p2 = list2

        x = int(input("enter position:"))
        y = int(input("enter the number to be entered from list2:"))        #taking position and value from player2
        print("postion and number to be entered: %d %d " % (x, y))
        board[x - 1] = y
        print(board)
        print(board[0], board[1], board[2])
        print(board[3], board[4], board[5])
        print(board[6], board[7], board[8])

        i = board[0] + board[1] + board[2]
        j = board[3] + board[4] + board[5]
        k = board[6] + board[7] + board[8]
        m = board[0] + board[3] + board[8]
        n = board[2] + board[3] + board[6]
    if (i == 15):
        print("player1 is winner")
    elif (j == 15):                                                        #checking sum to declare winner
        print("player1 is winner")
    elif (k == 15):
        print("player1 is winner")
    elif (m == 15):
        print("player1 is winner")
    elif (n == 15):
        print("player1 is winner")


    s= input("enter d for exit and f for continue")                         #options to continue or quit
    if(s=="f"):
        continue
    else:
        break


