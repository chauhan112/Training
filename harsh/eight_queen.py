N = 8
board = [[0] * N for _ in range(N)]


def check(i, j):
    # checking vertically and horizontally
    for k in range(0, N):
        if board[i][k] == 1 or board[k][j] == 1:
            return True

    # checking diagonally
    for k in range(0, N):
        for l in range(0, N):
            if (k + l == i + j) or (k - l == i - j):
                if board[k][l] == 1:
                    return True
    return False


def eight_queens(n):
    if n == 0:
        return True
    for j in range(0, N):
        for k in range(0, N):
            if (not (check(j, k))) and (board[j][k] != 1):
                board[j][k] = 1
                if eight_queens(n - 1):    # if true
                    return True
                board[j][k] = 0
    return False


eight_queens(N)

for r in board:
    print(r)  # prints out rows one by one
