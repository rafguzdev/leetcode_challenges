b = [["5","1",".",".","7",".",".",".","."]
    ,["6",".",".","1","9","5",".",".","."]
    ,[".","9","8",".",".",".",".","6","."]
    ,["8",".",".",".","6",".",".",".","3"]
    ,["4",".",".","8",".","3",".",".","1"]
    ,["7",".",".",".","2",".",".",".","6"]
    ,[".","6",".",".",".",".","2","8","."]
    ,[".",".",".","4","1","9",".",".","5"]
    ,[".",".",".",".","8",".",".","7","9"]]


def valid_row(board):
    for row in board:
        new = [x for x in row if x != '.']
        new.sort()
        snew = list(set(new))
        snew.sort()
        if new != snew:
            return False
    return True


def fun(board):
    # row valid
    if not valid_row(board):
        return False
    # col valid
    new_board = []
    for i in range(9):
        new_board.append([])
        for j in range(9):
            new_board[i].append(board[j][i])
    if not valid_row(new_board):
        return False
    #  square valid
    new_board = []
    for i in range(9):
        for j in range(3):
            new_board.append([])
            index = int(i/3)*3+j
            part = board[i][j*3:j*3+3]
            new_board[index] += part
    new_board = new_board[:9]
    if not valid_row(new_board):
        return False
    return True


print(fun(b))
