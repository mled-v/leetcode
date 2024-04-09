"""
:type board: List[List[str]]
:rtype: bool

Determine if a 9 x 9 Sudoku board is valid. Only the filled cells need to be validated according to the following rules:

Each row must contain the digits 1-9 without repetition.
Each column must contain the digits 1-9 without repetition.
Each of the nine 3 x 3 sub-boxes of the grid must contain the digits 1-9 without repetition.
Note:

A Sudoku board (partially filled) could be valid but is not necessarily solvable.
Only the filled cells need to be validated according to the mentioned rules.
"""

rows = 9
columns = 9

def isValidRow(board):
    for row in board:
        for num in row:
            if row.count(num) > 1 and num != ".":
                return False
        
    return True

def isValidColumn(board):
    for i in range(columns):
        list = []
        for j in range(rows):
            if board[j][i] != ".":
                list.append(board[j][i])
        if len(set(list)) != len(list):
            return False 
        
    return True

def isValidBox(board):
    
    count_column = 0
    count_row = 0
    for i in range(3):
        
        for j in range(3):
            print(board[count_column][j])
            print(board[count_column + 1][j])
            print(board[count_column + 2][j])
        count_column += 3

    return

def isValidSudoku(board):

    return         

board = [["5","3",".",".","7",".",".",".","."]
        ,["6",".",".","1","9","5",".",".","."]
        ,[".","9","8",".",".",".",".","6","."]
        ,["8",".",".",".","6",".",".",".","3"]
        ,["41",".",".","8",".","3",".",".","1"]
        ,["7",".",".",".","2",".",".",".","6"]
        ,[".","6",".",".",".",".","2","8","."]
        ,[".",".",".","4","1","9",".",".","5"]
        ,[".",".",".",".","8",".",".","7","9"]]

row = ["5","3",".",".","7",".",".",".","."]

print(isValidBox(board))