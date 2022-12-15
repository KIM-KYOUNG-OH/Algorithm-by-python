def search(board, aloc, bloc, turn):
    y, x = 0, 0
    if turn % 2 == 0:
        y, x = aloc[0], aloc[1]
    else:
        y, x = bloc[0], bloc[1]

    dy = [-1, 0, 1, 0]
    dx = [0, -1, 0, 1]
    nloc = []
    for k in range(4):
        ny = y + dy[k]
        nx = x + dx[k]
        if 0 <= ny < len(board) and 0 <= nx < len(board[0]) and board[ny][nx] == 1:
            nloc.append([ny, nx])

    if not nloc:
        return [False, 0]
    elif aloc == bloc:
        return [True, 1]

    can_win = False
    min_turn = len(board) * len(board[0])
    max_turn = 0

    for pos in nloc:
        board[y][x] = 0
        if turn % 2 == 0:
            result, cnt = search(board, pos, bloc, turn + 1)
        else:
            result, cnt = search(board, aloc, pos, turn + 1)
        board[y][x] = 1

        if not result:
            can_win = True
            min_turn = min(min_turn, cnt + 1)
        elif not can_win:
            max_turn = max(max_turn, cnt + 1)

    cnt = min_turn if can_win else max_turn
    return can_win, cnt


def solution(board, aloc, bloc):
    result, cnt = search(board, aloc, bloc, 0)
    return cnt


print(solution([[1, 1, 1], [1, 1, 1], [1, 1, 1]], [1, 0], [1, 2]))