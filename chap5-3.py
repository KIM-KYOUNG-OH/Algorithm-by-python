from collections import deque


def bfs(matrix, y, x, visit):
    dx = [-1, 0, 1, 0]
    dy = [0, -1, 0, 1]
    global cnt
    queue = deque()
    queue.append((y, x))
    visit[y][x] = 1
    while queue:
        v = queue.popleft()
        for i in range(4):
            xx, yy = v[1] + dx[i], v[0] + dy[i]
            if xx < 0 or yy < 0 or xx >= m or yy >= n:
                continue
            elif matrix[yy][xx] == 0 and visit[yy][xx] == 0:
                visit[yy][xx] = 1
                queue.append((yy, xx))
    cnt += 1


n, m = map(int, input().split())
matrix = [list(map(int, list(input()))) for _ in range(n)]
visit = [[0] * m for _ in range(n)]
cnt = 0

for i in range(n):
    for j in range(m):
        if matrix[i][j] == 0 and visit[i][j] == 0:
            bfs(matrix, i, j, visit)

print(cnt)
