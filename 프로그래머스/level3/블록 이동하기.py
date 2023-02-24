from collections import deque

dy = [-1, 0, 1, 0]
dx = [0, 1, 0, -1]


def can_move(cur1, cur2, fixed_board):
    y, x = 0, 1
    candidates = []
    for k in range(4):
        na = (cur1[y] + dy[k], cur1[x] + dx[k])
        nb = (cur2[y] + dy[k], cur2[x] + dx[k])
        if fixed_board[na[y]][na[x]] == 0 and fixed_board[nb[y]][nb[x]] == 0:
            candidates.append((na, nb))

    # 회전
    if cur1[y] == cur2[y]:  # 가로 방향일 때
        up, down = -1, 1
        for d in [up, down]:
            if fixed_board[cur1[y] + d][cur1[x]] == 0 and fixed_board[cur2[y] + d][cur2[x]] == 0:
                candidates.append((cur1, (cur1[y] + d, cur1[x])))
                candidates.append((cur2, (cur2[y] + d, cur2[x])))
    else:  # 세로 방향일 때
        left, right = -1, 1
        for d in [left, right]:
            if fixed_board[cur1[y]][cur1[x] + d] == 0 and fixed_board[cur2[y]][cur2[x] + d] == 0:
                candidates.append(((cur1[y], cur1[x] + d), cur1))
                candidates.append(((cur2[y], cur2[x] + d), cur2))
    return candidates


def solution(board):
    n = len(board)
    fixed_board = [[1] * (n + 2) for _ in range(n + 2)]
    for i in range(n):
        for j in range(n):
            fixed_board[i + 1][j + 1] = board[i][j]

    q = deque()
    q.append(((1, 1), (1, 2), 0))
    confirm = set()
    confirm.add(((1, 1), (1, 2)))

    while q:
        cur1, cur2, count = q.popleft()
        if cur1 == (n, n) or cur2 == (n, n):
            return count
        for next in can_move(cur1, cur2, fixed_board):
            if next not in confirm:
                q.append((*next, count + 1))
                confirm.add(next)


print(solution([[0, 0, 0, 1, 1], [0, 0, 0, 1, 0], [0, 1, 0, 1, 1], [1, 1, 0, 0, 1], [0, 0, 0, 0, 0]]))