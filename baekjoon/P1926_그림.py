import sys
from collections import deque

dy = [-1, 0, 1, 0]
dx = [0, 1, 0, -1]

n, m = map(int, sys.stdin.readline().rstrip().split())
matrix = [[] for _ in range(n)]
for i in range(n):
    matrix[i] = list(map(int, sys.stdin.readline().rstrip().split()))

cnt = 0
max_area = 0
visit = [[False] * m for _ in range(n)]
for i in range(n):
    for j in range(m):
        if visit[i][j]:
            continue
        elif matrix[i][j] == 0:
            continue
        visit[i][j] = True
        q = deque()
        q.append([i, j])
        area = 0
        while q:
            y, x = q.popleft()
            area += 1
            for k in range(4):
                ny = y + dy[k]
                nx = x + dx[k]
                if 0 <= ny < n and 0 <= nx < m:
                    if not visit[ny][nx] and matrix[ny][nx] == 1:
                        visit[ny][nx] = True
                        q.append([ny, nx])
        cnt += 1
        max_area = max(max_area, area)

print(cnt)
print(max_area)
