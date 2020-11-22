from sys import stdin
from collections import deque


def bfs(matrix, q):
    cnt = -1
    dx, dy = [1, -1, 0, 0], [0, 0, -1, 1]
    while q:
        for _ in range(len(q)):
            r, c = q.popleft()
            for k in range(4):
                rr, cc = r + dx[k], c + dy[k]
                if 0 <= rr < n and 0 <= cc < m:
                    if matrix[rr][cc] == 0:
                        matrix[rr][cc] = 1
                        q.append((rr, cc))
        cnt += 1
    for row in matrix:
        if 0 in row:
            return -1
    return cnt


m, n = map(int, stdin.readline().split())
box = []
queue = deque()
for i in range(n):
    row = list(map(int, list(stdin.readline().split())))
    for j in range(m):
        if row[j] == 1:
            queue.append((i, j))
    box.append(row)

print(bfs(box, queue))
