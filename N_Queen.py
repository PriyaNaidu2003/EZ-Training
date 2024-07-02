def is_safe(board, row, col):

    if any(board[row][i] == 1 for i in range(col)):
        return False


    if any(board[i][col] == 1 for i in range(row)):
        return False


    if any(board[i][j] == 1 for i, j in zip(range(row, -1, -1), range(col, -1, -1))):
        return False


    if any(board[i][j] == 1 for i, j in zip(range(row, len(board), 1), range(col, -1, -1))):
        return False

    return True


def solve_n_queens_util(board, col):
    """ Recursive utility function to solve N-Queens problem """
    n = len(board)

    if col >= n:
        return True

    for i in range(n):
        if is_safe(board, i, col):
            board[i][col] = 1

            if solve_n_queens_util(board, col + 1):
                return True

            board[i][col] = 0

    return False


def solve_n_queens(n):
    """ Solve the N-Queens problem for a given board size n x n """
    board = [[0] * n for _ in range(n)]

    if not solve_n_queens_util(board, 0):
        print("Solution does not exist")
        return False

    print_board(board)
    return True


def print_board(board):

    n = len(board)
    for i in range(n):
        for j in range(n):
            print(board[i][j], end=" ")
        print()


# Example usage:
n = 4
solve_n_queens(n)







