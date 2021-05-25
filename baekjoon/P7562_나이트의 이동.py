import sys
from collections import deque


def bfs(length, s_y, s_x, f_y, f_x):
    matrix = [[0] * length for _ in range(length)]

    dy = [2, 2, -2, -2, 1, 1, -1, -1]
    dx = [1, -1, 1, -1, 2, -2, 2, -2]

    q = deque([(0, s_y, s_x)])
    matrix[s_y][s_x] = 1
    while q:
        cnt, y, x = q.popleft()
        if y == f_y and x == f_x:
            return cnt
        for i in range(8):
            yy, xx = y + dy[i], x + dx[i]
            if 0 <= yy < length and 0 <= xx < length and matrix[yy][xx] == 0:
                matrix[yy][xx] = 1
                q.append((cnt + 1, yy, xx))


t = int(sys.stdin.readline().rstrip())
for _ in range(t):
    l = int(sys.stdin.readline().rstrip())
    start_y, start_x = map(int, sys.stdin.readline().rstrip().split())
    fin_y, fin_x = map(int, sys.stdin.readline().rstrip().split())
    print(bfs(l, start_y, start_x, fin_y, fin_x))
