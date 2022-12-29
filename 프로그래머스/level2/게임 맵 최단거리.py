from collections import deque


dy = [-1, 0, 1, 0]
dx = [0, 1, 0, -1]


def solution(maps):
    n = len(maps)
    m = len(maps[0])
    matrix = [[0 for _ in range(m)] for _ in range(n)]
    visited = [[False for _ in range(m)] for _ in range(n)]
    for i in range(n):
        for j in range(m):
            if maps[i][j] == 0:
                visited[i][j] = True
    q = deque()
    q.append([0, 0])
    visited[0][0] = True
    matrix[0][0] = 1
    while q:
        y, x = q.popleft()
        for k in range(4):
            ny = y + dy[k]
            nx = x + dx[k]
            if 0 <= ny < n and 0 <= nx < m:
                if not visited[ny][nx]:
                    matrix[ny][nx] = matrix[y][x] + 1
                    visited[ny][nx] = True
                    q.append([ny, nx])
    if matrix[n - 1][m - 1] == 0:
        return -1
    else:
        return matrix[n - 1][m - 1]


print(solution([[1,0,1,1,1],[1,0,1,0,1],[1,0,1,1,1],[1,1,1,0,1],[0,0,0,0,1]]))
