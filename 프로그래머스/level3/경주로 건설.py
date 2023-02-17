import sys
from collections import deque

dy = [-1, 0, 1, 0]
dx = [0, 1, 0, -1]


def solution(board):
    n = len(board)
    INF = sys.maxsize
    matrix = [[[INF] * 4 for _ in range(n)] for _ in range(n)]
    q = deque()
    if board[0][1] == 0:
        q.append([0, 1, 1, 100])
        matrix[0][0][1] = 100
        matrix[0][1][3] = 100
    if board[1][0] == 0:
        q.append([1, 0, 2, 100])
        matrix[0][0][2] = 100
        matrix[1][0][0] = 100

    while q:
        y, x, prev_dir, prev_cost = q.popleft()
        if y == n - 1 and x == n - 1:
            continue
        for k in range(4):
            opposite = (k + 2) % 4
            if opposite == prev_dir:
                continue
            ny = y + dy[k]
            nx = x + dx[k]
            cost = prev_cost
            if k == prev_dir:
                cost += 100
            else:
                cost += 600
            if 0 <= ny < n and 0 <= nx < n:
                if board[ny][nx] == 0 and cost < matrix[ny][nx][opposite]:
                    q.append([ny, nx, k, cost])
                    matrix[y][x][k] = cost
                    matrix[ny][nx][opposite] = cost
    return min(matrix[n - 1][n - 1])


# print(solution([[0,0,0],[0,0,0],[0,0,0]]))
# print(solution([[0,0,0,0,0,0,0,1],[0,0,0,0,0,0,0,0],[0,0,0,0,0,1,0,0],[0,0,0,0,1,0,0,0],[0,0,0,1,0,0,0,1],[0,0,1,0,0,0,1,0],[0,1,0,0,0,1,0,0],[1,0,0,0,0,0,0,0]]))
# print(solution([[0,0,1,0],[0,0,0,0],[0,1,0,1],[1,0,0,0]]))
print(solution([[0,0,0,0,0,0],[0,1,1,1,1,0],[0,0,1,0,0,0],[1,0,0,1,0,1],[0,1,0,0,0,1],[0,0,0,0,0,0]]))