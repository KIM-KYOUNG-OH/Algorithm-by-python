from collections import deque


def bfs(matrix: list, n: int, m: int):
    answer = -1
    dy = [-1, 0, 1, 0]
    dx = [0, -1, 0, 1]
    visited = [[False for _ in range(m)] for _ in range(n)]
    q = deque()
    q.append([0, 0])
    visited[0][0] = True
    while q:
        y, x = q.popleft()
        if y == n - 1 and x == m - 1:
            return matrix[-1][-1]
        for k in range(4):
            ny = y + dy[k]
            nx = x + dx[k]
            if 0 <= ny < n and 0 <= nx < m:
                if matrix[ny][nx] != -1 and not visited[ny][nx]:
                    visited[ny][nx] = True
                    matrix[ny][nx] += matrix[y][x]
                    q.append([ny, nx])
    return answer


def solution(maps):
    n = len(maps)
    m = len(maps[0])
    matrix = [[1 for _ in range(m)] for _ in range(n)]
    for i in range(n):
        for j in range(m):
            if maps[i][j] == 0:
                matrix[i][j] = -1
    answer = bfs(matrix, n, m)
    return answer


print(solution([[1,0,1,1,1],[1,0,1,0,1],[1,0,1,1,1],[1,1,1,0,1],[0,0,0,0,1]]))