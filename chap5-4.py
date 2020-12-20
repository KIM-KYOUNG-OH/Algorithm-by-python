from collections import deque


def bfs(matrix, y, x, visit):
    visit[y][x] = True
    queue = deque([(y, x)])
    while queue:
        v = queue.popleft()
        for i in range(4):
            xx = v[1] + dx[i]
            yy = v[0] + dy[i]
            if xx < 0 or yy < 0 or xx >= m or yy >= n:
                continue
            elif visit[yy][xx] == False and matrix[yy][xx] == 1:
                visit[yy][xx] = True
                matrix[yy][xx] = matrix[v[0]][v[1]] + 1
                queue.append((yy, xx))


n, m = map(int, input().split())
matrix = [list(map(int, list(input()))) for _ in range(n)]
visit = [[False] * m for _ in range(n)]
y, x = 0, 0
dx, dy = [-1, 0, 1, 0], [0, -1, 0, 1]
bfs(matrix, y, x, visit)
print(matrix[n - 1][m - 1])
