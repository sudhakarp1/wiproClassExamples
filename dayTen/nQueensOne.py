def validate(board, row, col, n):
    for i in range(row):
        if board[i][col]== 1:
            return False 
    
    for i, j in zip(range(row,-1,-1), range(col,-1,-1)):
        if board[i][j] == 1:
            return False

    for i, j in zip(range(row,-1,-1), range(col,n)):
        if board[i][j] == 1:
            return False
        
    return True


def solveQueens(board, row, n ,result):
    if row == n:
        result.append([row[:] for row in board])
        return
    
    for col in range(n):
        if validate(board, row,col, n):
            board[row][col] = 1
            solveQueens(board, row + 1, n , result)
            board[row][col] = 0


def NQueens(n):
    board = [[0] * n for _ in range(n)]
    result = []
    solveQueens(board, 0,n, result)
    return result

    
def printSolution(solution):
    if not solution:
        print('No solution exists')
        return 
    #print(solution)
    
    for board in solution:        
        for row in board:
            #print(row)
            print(' '.join('Q' if cell == 1 else 'x' for cell in row))
        print()

if __name__ == '__main__':
    n = 4
    solutions = NQueens(n)
    printSolution(solutions)