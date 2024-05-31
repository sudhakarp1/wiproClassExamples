def isValidMove(board, i, j):
    return 0 <= i < len(board) and 0 <= j < len(board[0]) and board[i][j] == -1

def printBoard(board, n):
    for i in range(n):
        for j in range(n):
            print(f'{board[i][j]:2}', end= '  ')
        print()

def solveKnightTour(board, n, i, j, pos, moves):
    if pos == n ** 2:
        return True
    
    for i in range(8):
        newI, newJ = i + moves[i][0], j + moves[i][1]
        if isValidMove(board, newI, newJ):
            #print(f'board[{newI}][{newJ}] = {pos}')
            board[newI][newJ] = pos
            if solveKnightTour(board, n, newI, newJ, pos + 1, moves):
                print(board)
                return True
            
            board[newI][newJ] = -1
    return False

def knightTour(n):
    board =[[-1 for i in range(n)] for j in range(n)]
    #printBoard(board, n)
    #starting point is 0,0
    directions = [(1,2),(1,-2),(2,1),(2,-1),(-1,2),(-1,-2),(-2,1),(-2,-1)]
    
    board[0][0] = 0
    pos = 1
    if not solveKnightTour(board, n, 0,0,pos, directions):
        print('Solution Dose not exist')
    else:        
        printBoard(board, n)

    #printBoard(board,n)
if __name__ == '__main__':
    knightTour(8)
