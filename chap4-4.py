n, m = map(int, input().split())
y, x, dir = map(int, input().split())
matrix = [list(map(int, input().split())) for _ in range(n)]
visit = [[0] * m for _ in range(n)]
visit[y][x] = 1
dx = [0, 1, 0, -1]
dy = [-1, 0, 1, 0]

def turn_left():
    global dir
    dir -= 1
    if dir == -1:
        dir = 3

cnt = 1
turn_cnt = 0
while True:
    turn_left()
    xx = x + dx[dir]
    yy = y + dy[dir]
    if visit[yy][xx] == 0 and matrix[yy][xx] == 0:
        visit[yy][xx] = 1
        x, y = xx, yy
        cnt += 1
        turn_cnt = 0
        continue
    else:
        turn_cnt += 1
    if turn_cnt == 4:
        xx = x - dx[dir]
        yy = y - dy[dir]
        if matrix[yy][xx] == 0:
            x, y = xx, yy
            turn_cnt = 0
        else:
            break
print(cnt)