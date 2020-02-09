from os import system

globalBoard = None


def defineBoard():
    x = 7
    y = 6
    board = [[' '] * x for i in range(y)]
    return board


def drawBoard(board):
    system('cls')
    print()
    header = ''
    for i in range(7):
        header = header + ('  ' + str(i) + '  ')
    print(header)
    for x in board:
        print(x)
    print()


def checkCol(board, col):
    if board[0][col] != ' ':
        print('Column full!')
        return False
    else:
        return True


def dropPiece(board, col, turn):
    for i, x in enumerate(board):
        if x[col] != ' ':
            board[i - 1][col] = turn
            return True

    board[5][col] = turn
    return True


def checkWinner(board, turn):
    # Horizontal Check
    for x in board:
        checkingCount = 0
        for y in x:
            if y == turn:
                checkingCount = checkingCount + 1
                if checkingCount == 4:
                    return True
            else:
                checkingCount = 0

    # Vertical Check
    for i in range(6):
        checkingCount = 0
        for x in board:
            if x[i] == turn:
                checkingCount = checkingCount + 1
                if checkingCount == 4:
                    return True
            else:
                checkingCount = 0

    # Diagonal Check
    for i in range(3, 6):
        for j in range(0, 4):
            if board[i][j] == turn and board[i-1][j+1] == turn \
                    and board[i-2][j+2] == turn and board[i-3][j+3] == turn:
                return True

    for i in range(3, 6):
        for j in range(3, 6):
            if board[i][j] == turn and board[i-1][j-1] == turn \
                    and board[i-2][j-2] == turn and board[i-3][j-3] == turn:
                return True

    return False


def changeTurn(turn):
    if turn == 'X':
        return 'O'
    else:
        return 'X'


def gameloop(board):
    turn = 'X'
    while True:
        drawBoard(board)
        while True:
            col = int(input('Select a column to drop your piece: '))
            if col == 9:
                exit()
            if checkCol(board, col):
                dropPiece(board, col, turn)
                break
        if checkWinner(board, turn):
            break
        turn = changeTurn(turn)

    drawBoard(board)
    print(turn + ' wins!')
