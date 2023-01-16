import sys
from collections import deque

dy = [-1, 0, 1, 0]
dx = [0, 1, 0, -1]

n = int(sys.stdin.readline().rstrip())
matrix = []
max_val = 0
for _ in range(n):
    tmp = list(map(int, sys.stdin.readline().rstrip().split()))
    matrix.append(tmp)
    max_val = max(max_val, max(tmp))

answer = 0
for k in range(max_val):
    isWet = [[False] * n for _ in range(n)]
    for i in range(n):
        for j in range(n):
            if matrix[i][j] <= k:
                isWet[i][j] = True

    cnt = 0
    q = deque()
    for i in range(n):
        for j in range(n):
            if isWet[i][j]:
                continue
            cnt += 1
            q.append([i, j])
            isWet[i][j] = True
            while q:
                y, x = q.popleft()
                for g in range(4):
                    ny = y + dy[g]
                    nx = x + dx[g]
                    if 0 <= ny < n and 0 <= nx < n:
                        if not isWet[ny][nx]:
                            isWet[ny][nx] = True
                            q.append([ny, nx])
    answer = max(answer, cnt)
print(answer)
