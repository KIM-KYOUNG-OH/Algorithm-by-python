def solution(m, n, board):
    board = [list(x) for x in board]

    cnt = 0
    rm = set()
    while True:
        for i in range(m - 1):
            for j in range(n - 1):
                ch = board[i][j]
                if ch is None:
                    continue
                if board[i + 1][j] == ch and board[i][j + 1] == ch and board[i + 1][j + 1] == ch:
                    rm.add((i, j))
                    rm.add((i, j + 1))
                    rm.add((i + 1, j))
                    rm.add((i + 1, j + 1))
        if rm:
            cnt += len(rm)
            for i, j in rm:
                board[i][j] = None
            rm = set()
        else:
            return cnt

        while True:
            moved = 0
            for i in range(m - 1):
                for j in range(n):
                    if board[i][j] and board[i + 1][j] is None:
                        board[i + 1][j] = board[i][j]
                        board[i][j] = None
                        moved = 1
            if moved == 0:
                break


solution(6, 6, ["TTTANT", "RRFACC", "RRRFCC", "TRRRAA", "TTMMMF", "TMMTTJ"])