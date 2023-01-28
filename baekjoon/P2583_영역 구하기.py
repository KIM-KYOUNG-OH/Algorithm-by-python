import sys
from collections import deque

dy = [-1, 0, 1, 0]
dx = [0, 1, 0, -1]

m, n, k = map(int, sys.stdin.readline().rstrip().split())
matrix = [[0] * n for _ in range(m)]
for _ in range(k):
    lx, ly, rx, ry = map(int, sys.stdin.readline().rstrip().split())
    for i in range(ly, ry):
        for j in range(lx, rx):
            matrix[i][j] = 1

areas = []
for i in range(m):
    for j in range(n):
        if matrix[i][j] == 0:
            matrix[i][j] = 1
            q = deque()
            q.append([i, j])
            area = 1
            while q:
                y, x = q.popleft()
                for k in range(4):
                    ny = y + dy[k]
                    nx = x + dx[k]
                    if 0 <= ny < m and 0 <= nx < n:
                        if matrix[ny][nx] == 0:
                            area += 1
                            matrix[ny][nx] = 1
                            q.append([ny, nx])
            areas.append(area)
areas.sort()
print(len(areas))
print(' '.join(map(str, areas)))

