def validataMove(maze, i, j):
    isValid = 0 <= i < len(maze) and 0 <= j < len(maze[0]) and maze[i][j] == 1
    return isValid

def solveMaze(maze, i, j, solution):# maze, 1, 0 , solution
    if i == len(maze) - 1 and j == len(maze[0]) - 1:
        solution[i][j] = 1
        return True 

    if validataMove(maze, i, j): # maze, 0, 0
        solution[i][j] = 1
        
        directions = [(1, 0), (0, 1), (0,-1), (-1, 0)]
        for di, dj in directions:
            nextI, nextJ  = i + di, j+ dj   # 0+1, 0+0         
            if solveMaze(maze, nextI, nextJ, solution):
                return True
            
        solution[i][j] = 0
        return False
    return False

def ratInAMaze(maze):    
    if not maze:
        return []
    
    solution = [[0]*len(maze[0]) for _ in range(len(maze))]
    if solveMaze(maze, 0, 0, solution):
        return solution
    
    return []


if __name__ == '__main__':
    maze = [ 
        [ 1, 1, 1, 0],
        [ 1, 0, 0, 0],
        [ 1, 1, 0, 0],
        [ 0, 1, 1, 1]
    ] 

    print('Maze')
    for row in maze:
        print(row)
    
    print('*' * 30)

    solution = ratInAMaze(maze)

    if solution:
        print('solution')
        for row in solution:
            print(row)
    else:
        print('No Solution Exists')