from collections import deque

n, m = map(int, input().split())
matrix = [list(map(int, list(input()))) for _ in range(n)]
visit = [[False] * m for _ in range(n)]
result = [[0] * m for _ in range(n)]
q = deque()

visit[0][0] = True
result[0][0] = 1
q.append((0, 0))
dx, dy = [-1,1,0,0], [0,0,-1,1]

while q:
    x, y = q.popleft()
    for j in range(4):
        xx, yy = x + dx[j], y + dy[j]
        if 0<= xx < n and 0<= yy < m:
            if matrix[xx][yy] == 1 and visit[xx][yy] == False:
                result[xx][yy] = result[x][y] + 1
                q.append((xx, yy))
                visit[xx][yy] = True

print(result[n-1][m-1])