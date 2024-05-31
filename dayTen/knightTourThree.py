def isValidMove(board, i, j):
    return 0 <=i <len(board) and 0 <= j < len(board[0]) and board[i][j] == -1

 
def printBoard(board, n):
    for i in range(n):
        for j in range(n):
            print(f'{board[i][j]:2}', end=' ')
        print()
 
def solveKnightTour(board, n, i, j,pos,moves):
    if pos == n**2:
        return True
   
    for d in moves:
        newI, newJ = i+d[0], j+d[1]
        if isValidMove(board, newI, newJ):
            board[newI][newJ]  = pos
            if solveKnightTour(board, n, newI, newJ, pos+1, moves):
                return True
           
            board[newI][newJ] = -1
    return False
 
 
def knighTour(n):
    board = [[-1 for i in range(n)] for _ in range(n)]
    printBoard(board,n)
 
    directions = [(2,1), (1,2), (-1,2), (-2,1), (-2,-1), (-1,-2), (1,-2), (2,-1)]
    pos=1
    board[0][0] =0
    if  solveKnightTour(board, n,0,0,pos, directions):
        printBoard(board, n)
    else:
        print('Solution does not exists')
 
 
 
if __name__ == '__main__':
    #n = 8
    knighTour(8)