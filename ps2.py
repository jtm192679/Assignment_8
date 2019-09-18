print("welcome to the game")
list1 = [1, 3, 5, 7, 9]
list2 = [2, 4, 6, 8]
board = [0, 0, 0, 0, 0, 0, 0, 0, 0]
print(board[0], board[1], board[2])
print(board[2], board[3], board[4])
print(board[6], board[7], board[8])
while [True]:
    n = int(input("press 1 for player1's chance  and press 2 for player2's chance:"))
    if (n == 1):
        print("player1's chgance")
        p1 = list1

        a = int(input("enter the position:"))
        b = int(input("enter the number to be entered from list1:"))
        print("postion and number to be entered: %d %d " % (a, b))

        board[a - 1] = b
        print(board)
        p = int(input("press 2 for player2's chance:"))
    if (p == 2):
        p2 = list2

        x = int(input("enter position:"))
        y = int(input("enter the number to be entered from list2:"))
        print("postion and number to be entered: %d %d " % (x, y))
        board[x - 1] = y
        print(board)
