def is_valid_move(board, move, n):
    x, y = move
    if 0 <= x < n and 0 <= y < n and board[x][y] == -1:
        return True
    return False

def knight_tour(n):
    board = [[-1 for _ in range(n)] for _ in range(n)]
    moves = [(2, 1), (1, 2), (-1, 2), (-2, 1),
             (-2, -1), (-1, -2), (1, -2), (2, -1)]

    def helper(board, move_number, x, y):
        if move_number == n ** 2:
            return True

        for dx, dy in moves:
            next_x, next_y = x + dx, y + dy
            if is_valid_move(board, (next_x, next_y), n):
                board[next_x][next_y] = move_number
                if helper(board, move_number + 1, next_x, next_y):
                    return True
                board[next_x][next_y] = -1

        return False

    start_x, start_y = 0,0
    board[start_x][start_y] = 0

    if helper(board, 1, start_x, start_y):
        return board
    else:
        return None

def print_board(board):
    if board is None:
        print("No solution exists.")
        return
    for row in board:
        print(' '.join(str(cell).zfill(2) for cell in row))

if __name__ =='__main__':
    solution = knight_tour(8)
    print_board(solution)
