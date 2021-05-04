from collections import deque

n, k = map(int, input().split())
matrix = []
q = []
for i in range(n):
    matrix.append(list(map(int, input().split())))
    for j in range(n):
        if matrix[i][j] != 0:
            # (virus 종류, time, x, y)
            q.append((matrix[i][j], 0, i, j))
target_s, target_x, target_y = map(int, input().split())
q.sort()
q = deque(q)

dx = [-1, 0, 1, 0]
dy = [0, -1, 0, 1]

while q:
    v, t, x, y = q.popleft()
    if t == target_s:
        break
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        if 0 <= nx < n and 0 <= ny < n:
            if matrix[nx][ny] == 0:
                matrix[nx][ny] = v
                q.append((v, t + 1, nx, ny))
print(matrix[target_x - 1][target_y - 1])
