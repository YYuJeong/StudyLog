def solution(m, n, board):
    score = 0

    arr = [(0, 1), (1, 0), (1, 1)]

    board = [list(row) for row in board]

    while True:
        delete = set([])
        for i in range(m-1):
            for j in range(n-1):
                cnt = 0
                if board[i][j] == '#':
                    continue
                if all(board[i][j] == board[i+xi][j+yi] for (xi, yi) in arr):
                    delete.update([(i, j), (i+1, j), (i, j+1), (i+1, j+1)])

        if len(delete) == 0:
            return score
        score += len(delete)
        for (i, j) in delete:
            board[i][j] = '#'

        delete = set([])

        while True:
            move = 0
            for i in range(m-1):
                for j in range(n):
                    if board[i][j] != '#' and board[i+1][j] == '#':
                        move = 1
                        board[i+1][j] = board[i][j]
                        board[i][j] = '#'
            if move == 0:
                break
