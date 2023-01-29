import sys
from collections import deque

dy = [-1, 0, 1, 0]
dx = [0, 1, 0, -1]


def bfs(visit, i, j):
    q = deque()
    q.append([i, j])
    unit = [[i, j]]
    while q:
        y, x = q.popleft()
        # print('y = ', y, ', x = ', x)
        for k in range(4):
            ny = y + dy[k]
            nx = x + dx[k]
            if 0 <= ny < n and 0 <= nx < n and not visit[ny][nx]:
                if l <= abs(matrix[y][x] - matrix[ny][nx]) <= r:
                    visit[ny][nx] = True
                    q.append([ny, nx])
                    unit.append([ny, nx])
    return unit


n, l, r = map(int, sys.stdin.readline().rstrip().split())
matrix = []
for _ in range(n):
    matrix.append(list(map(int, sys.stdin.readline().rstrip().split())))

answer = 0
while True:
    isChanged = False
    visit = [[False] * n for _ in range(n)]
    for i in range(n):
        for j in range(n):
            if visit[i][j]:
                continue
            visit[i][j] = True
            unit = bfs(visit, i, j)

            if len(unit) > 1:
                value = sum([matrix[y][x] for y, x in unit]) // len(unit)
                isChanged = True
                for y, x in unit:
                    matrix[y][x] = value

    if not isChanged:
        break
    answer += 1
print(answer)
