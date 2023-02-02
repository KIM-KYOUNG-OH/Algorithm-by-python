import sys
from collections import deque

dy = [-1, 0, 1, 0]
dx = [0, 1, 0, -1]


def getRedAndBlue(n, m):
    pos = [-1, -1, -1, -1]
    for i in range(n):
        for j in range(m):
            if pos[0] != -1 and pos[2] != -1:
                return pos
            if matrix[i][j] == 'R':
                pos[0] = i
                pos[1] = j
            elif matrix[i][j] == 'B':
                pos[2] = i
                pos[3] = j
    return pos


n, m = map(int, sys.stdin.readline().rstrip().split())
matrix = []
o = [0, 0]
for i in range(n):
    temp = list(sys.stdin.readline().rstrip())
    if 'O' in temp:
        o = [i, temp.index('O')]
    matrix.append(temp)

pos = getRedAndBlue(n, m)
history = dict()
q = deque()
q.append([tuple(pos), 0])
answer = 0


def getNextPos(y, x, k):
    cnt = 0
    while True:
        if matrix[y][x] == 'O':
            return y, x, cnt
        ny = y + dy[k]
        nx = x + dx[k]
        if matrix[ny][nx] == '#':
            return y, x, cnt
        y, x = ny, nx
        cnt += 1


while q:
    pos, cnt = q.popleft()
    if cnt > 10:
        break
    ry = pos[0]
    rx = pos[1]
    by = pos[2]
    bx = pos[3]
    # print('pos_ry = ', pos_ry, ', pos_rx = ', pos_rx, ', pos_by = ', pos_by, ', pos_bx = ', pos_bx)
    if ry == o[0] and rx == o[1]:
        answer = cnt
        break
    elif by == o[0] and bx == o[1]:
        continue

    for k in range(4):
        nry, nrx, move_r = getNextPos(ry, rx, k)
        nby, nbx, move_b = getNextPos(by, bx, k)

        # 겹칠때
        if nry == nby and nrx == nbx:
            if matrix[nry][nrx] == 'O':
                continue
            if move_r > move_b:
                nry -= dy[k]
                nrx -= dx[k]
            else:
                nby -= dy[k]
                nbx -= dx[k]

        if 0 <= nry < n and 0 <= nrx < m and 0 <= nby < n and 0 <= nbx <= m:
            if (nry, nrx, nby, nbx) not in history:
                # print('k = ', k)
                # print('ry = ', ry, ', rx = ', rx, ', by = ', by, ', bx = ', bx)
                history[(nry, nrx, nby, nbx)] = 0
                q.append([(nry, nrx, nby, nbx), cnt + 1])

if answer == 0:
    print(-1)
else:
    print(answer)
