import sys


def move_dice(direction):
    if direction == 1:  # 동
        dice[1], dice[3], dice[4], dice[6] = dice[4], dice[1], dice[6], dice[3]
    elif direction == 2:  # 서
        dice[1], dice[3], dice[4], dice[6] = dice[3], dice[6], dice[1], dice[4]
    elif direction == 3:  # 북
        dice[1], dice[2], dice[5], dice[6] = dice[5], dice[1], dice[6], dice[2]
    elif direction == 4:  # 남
        dice[1], dice[2], dice[5], dice[6] = dice[2], dice[6], dice[1], dice[5]


n, m, y, x, k = map(int, sys.stdin.readline().rstrip().split())  # y: 행, x: 열
arr = [list(map(int, sys.stdin.readline().rstrip().split())) for _ in range(n)]
orders = list(map(int, sys.stdin.readline().rstrip().split()))
dice = [0 for _ in range(7)]  # [0, 위, 북, 동, 서, 남, 아래]

dy = [0, 0, 0, -1, 1]  # [0, 동, 서, 북, 남]
dx = [0, 1, -1, 0, 0]

for i in orders:
    if 0 <= y + dy[i] < n and 0 <= x + dx[i] < m:
        y = y + dy[i]
        x = x + dx[i]
        move_dice(i)
        if arr[y][x] != 0:
            dice[6] = arr[y][x]
            arr[y][x] = 0
        else:
            arr[y][x] = dice[6]
        print(dice[1])
