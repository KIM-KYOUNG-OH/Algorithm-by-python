from collections import deque


dy = [-1, 0, 1, 0]
dx = [0, 1, 0, -1]


def solution(m, n, puddles):
    matrix = [[0 for _ in range(m + 1)] for _ in range(n + 1)]
    visited = [[False for _ in range(m + 1)] for _ in range(n + 1)]
    for x, y in puddles:
        visited[y][x] = True
    q = deque()
    q.append([1, 1])
    visited[1][1] = True
    matrix[1][1] = 1
    while q:
        y, x = q.popleft()
        for k in range(4):
            ny = y + dy[k]
            nx = x + dx[k]
            if 0 < ny <= n and 0 < nx <= m:
                if not visited[ny][nx]:
                    matrix[ny][nx] = matrix[ny - 1][nx] + matrix[ny][nx - 1]
                    visited[ny][nx] = True
                    q.append([ny, nx])
    return matrix[n][m] % 1000000007


print(solution(4, 3, [[2, 2]]))

