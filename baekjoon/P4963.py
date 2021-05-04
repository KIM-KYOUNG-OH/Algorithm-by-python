from collections import deque


def bfs(start_r, start_c, h, w):
    dx = [-1, 0, 1, 0, -1, -1, 1, 1]
    dy = [0, -1, 0, 1, 1, -1, -1, 1]
    q = deque([(start_r, start_c)])
    visited[start_r][start_c] = True
    while q:
        x, y = q.popleft()
        for i in range(8):
            xx = x + dx[i]
            yy = y + dy[i]
            if 0 <= xx < h and 0 <= yy < w:
                if not visited[xx][yy] and matrix[xx][yy] == 1:
                    visited[xx][yy] = True
                    q.append((xx, yy))


while True:
    wide, heigth = map(int, input().split())
    if wide == 0 and heigth == 0:
        break
    matrix = []
    visited = [[False] * wide for _ in range(heigth)]
    for _ in range(heigth):
        matrix.append(list(map(int, input().split())))
    cnt = 0
    for i in range(heigth):
        for j in range(wide):
            if matrix[i][j] == 1 and not visited[i][j]:
                bfs(i, j, heigth, wide)
                cnt += 1
    print(cnt)