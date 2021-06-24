import sys


def move_dice(direction):
    if direction == 1:
        dice[1], dice[3], dice[4], dice[6] = dice[3], dice[6], dice[1], dice[4]
    elif direction == 2:
        dice[1], dice[3], dice[4], dice[6] = dice[4], dice[1], dice[6], dice[3]
    elif direction == 3:
        dice[1], dice[2], dice[5], dice[6] = dice[2], dice[6], dice[1], dice[5]
    elif direction == 4:
        dice[1], dice[2], dice[5], dice[6] = dice[5], dice[1], dice[6], dice[2]


def dire(direction):
    if direction == 1:
        return 0, 1
    elif direction == 2:
        return 0, -1
    elif direction == 3:
        return -1, 0
    elif direction == 4:
        return 1, 0


n, m, y, x, k = map(int, sys.stdin.readline().rstrip().split())
arr = [list(map(int, sys.stdin.readline().rstrip().split())) for _ in range(n)]
orders = list(map(int, sys.stdin.readline().rstrip().split()))
dice = [0, 0, 0, 0, 0, 0, 0]

for i in orders:
    a, b = dire(i)
    if 0 <= y + a < n and 0 <= x + b < m:
        y += a
        x += b
        move_dice(i)
        if arr[y][x] != 0:
            dice[1] = arr[y][x]
            arr[y][x] = 0
        else:
            arr[y][x] = dice[1]
        print(dice[6])
