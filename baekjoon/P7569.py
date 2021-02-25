from sys import stdin
from collections import deque


def bfs(matrix, q):
    dx, dy, dz = [-1, 1, 0, 0, 0, 0], [0, 0, -1, 1, 0, 0], [0, 0, 0, 0, -1, 1]
    cnt = -1
    while q:
        for _ in range(len(q)):
            r, c, d = q.popleft()
            for i in range(6):
                rr, cc, dd = r + dx[i], c + dy[i], d + dz[i]
                if 0 <= rr < n and 0 <= cc < m and 0 <= dd < h:
                    if matrix[dd][rr][cc] == 0:
                        matrix[dd][rr][cc] = 1
                        q.append((rr, cc, dd))
        cnt += 1

    for i in matrix:
        for j in i:
            if 0 in j:
                return -1
    return cnt


m, n, h = map(int, stdin.readline().split())
matrix = []
q = deque()
for i in range(h):
    temp = []
    for j in range(n):
        row = list(map(int, list(stdin.readline().split())))
        for k in range(m):
            if row[k] == 1:
                q.append((j, k, i))
        temp.append(row)
    matrix.append(temp)

print(bfs(matrix, q))
