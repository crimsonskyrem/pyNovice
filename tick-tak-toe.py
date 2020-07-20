import random

def printBoard(board):
    print(board[6] + '|' + board[7] + '|' + board[8])
    print(board[3] + '|' + board[4] + '|' + board[5])
    print(board[0] + '|' + board[1] + '|' + board[2])

def isWinner(board,role):
    return ((board[0] == role and board[1] == role and board[2] == role) or
        (board[3] == role and board[4] == role and board[5] == role) or
        (board[6] == role and board[7] == role and board[8] == role) or
        (board[0] == role and board[3] == role and board[6] == role) or
        (board[1] == role and board[4] == role and board[7] == role) or
        (board[2] == role and board[5] == role and board[8] == role) or
        (board[0] == role and board[4] == role and board[8] == role) or
        (board[2] == role and board[4] == role and board[6] == role))

def isEven(board):
    for i in board:
        if i is '*':
            return False
    return True

def placable(board, pos):
    return board[pos] is '*'

def compCore(board, comp, player):
    flag = False
    for i in range(9):
        cpy = board.copy()
        if placable(cpy, i):
            cpy[i] = comp
            if isWinner(cpy, comp):
                board[i] = comp
                flag = True
                break
    if flag:
        return
    for i in range(9):
        cpy = board.copy()
        if placable(cpy, i):
            cpy[i] = player
            if isWinner(cpy, player):
                board[i] = comp
                flag = True
                break
    if flag:
        return 
    for i in [4,0,2,6,8,7,3,5,1]:
        if placable(board, i):
            board[i] = comp
            break
    return 

def play(board,player):
    while 1:
        ip = input()
        if ip is '':
            break
        else:
            pos = int(ip) - 1
            if placable(board,pos):
                board[pos] = player
                break
    return 


board = ['*'] * 9

comp = 'X' if random.randint(1,2) == 1 else 'O'
player = 'O' if comp is 'X' else 'X'
plyaerFirst = True if random.randint(1,2) == 1 else False

while 1:
    print('yours is ' + player)
    if plyaerFirst:
        play(board,player)
        compCore(board,comp,player)
        printBoard(board)
    else:
        compCore(board,comp,player)
        printBoard(board)
        play(board,player)
    if isWinner(board, comp):
        print('you lose')
        break
    if isWinner(board, player):
        print('you win')
        break
    if isEven(board):
        print('even')
        break