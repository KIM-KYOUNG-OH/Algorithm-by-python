import sys


def move(dir):
    if dir == 1:  # 동
        dice[1], dice[3], dice[6], dice[4] = dice[4], dice[1], dice[3], dice[6]
    if dir == 2:  # 서
        dice[1], dice[3], dice[6], dice[4] = dice[3], dice[6], dice[4], dice[1]
    if dir == 3:  # 


n, m, x, y, k = map(int, sys.stdin.readline().rstrip().split())
Map = []
for _ in range(n):
    Map.append(list(map(int, sys.stdin.readline().rstrip().split())))
orders = list(map(int, sys.stdin.readline().rstrip().split()))

dice = [0] * 7  # [0, 위, 북, 동, 서, 남, 밑]

dy = [0, 0, 0, -1, 1]  # [0, 동, 서, 북, 남]
dx = [0, 1, -1, 0, 0]

for i in range(len(orders)):
    ny = y + dy[orders[i]]
    nx = x + dx[orders[i]]
    if 0 <= ny < n and 0 <= nx < m:
