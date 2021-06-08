import sys
from collections import deque


def bfs():
    q = deque([(0, 0, 1)])
    visited = [[[0] * 2 for _ in range(m)] for _ in range(n)]
    visited[0][0][1] = 1
    while q:
        y, x, smash = q.popleft()  # smash가 1이면 벽을 뚫을 수 있다
        if y == n - 1 and x == m - 1:
            return visited[y][x][smash]
        for i in range(4):
            yy = y + dy[i]
            xx = x + dx[i]
            if 0 <= yy < n and 0 <= xx < m:
                if matrix[yy][xx] == 1 and smash == 1:
                    visited[yy][xx][0] = visited[y][x][1] + 1
                    q.append((yy, xx, 0))
                elif matrix[yy][xx] == 0 and visited[yy][xx][smash] == 0:
                    visited[yy][xx][smash] = visited[y][x][smash] + 1
                    q.append((yy, xx, smash))
    return -1


n, m = map(int, sys.stdin.readline().rstrip().split())
matrix = []
for _ in range(n):
    s = list(map(int, list(sys.stdin.readline().rstrip())))
    matrix.append(s)

dy = [-1, 0, 1, 0]
dx = [0, -1, 0, 1]

print(bfs())
