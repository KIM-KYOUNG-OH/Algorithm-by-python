n = int(input())
k = int(input())
field = [[0] * (n + 1) for _ in range(n + 1)]
direction_data = []
for _ in range(k):
    a, b = map(int, input().split())
    field[a][b] = 1

l = int(input())
for _ in range(l):
    a, b = input().split()
    direction_data.append((int(a), b))

dx = [1, 0, -1, 0]  # 동 남 서 북
dy = [0, 1, 0, -1]


def turn(direction, alp):
    if alp == 'L':
        direction = (direction - 1) % 4
    else:
        direction = (direction + 1) % 4
    return direction


def simulation():
    r, c = 1, 1
    direction = 0
    time = 0
    index = 0  # direction_data의 index
    q = [(r, c)]
    while True:
        print(field)
        nr = r + dy[direction]
        nc = c + dx[direction]
        if 0 < nr <= n and 0 < nc <= n and field[nr][nc] != 2:
            if field[nr][nc] == 0:
                field[nr][nc] = 2
                q.append((nr, nc))
                pr, pc = q.pop(0)
                field[pr][pc] = 0
            elif field[nr][nc] == 1:
                field[nr][nc] = 2
                q.append((nr, nc))
        else:
            time += 1
            break
        r, c = nr, nc
        time += 1
        if time == direction_data[index][0]:
            direction = turn(direction, direction_data[index][1])
            index += 1
    return time


print(simulation())
