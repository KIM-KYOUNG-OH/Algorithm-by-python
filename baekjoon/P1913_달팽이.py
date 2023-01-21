import sys

n = int(sys.stdin.readline().rstrip())
target = int(sys.stdin.readline().rstrip())
matrix = [[0] * (n + 1) for _ in range(n + 1)]
cy, cx = 0, 0
if n == 3:
    cy, cx = 1, 1
else:
    cy, cx = n // 2 + 1, n // 2 + 1
num = 1
matrix[cy][cx] = num
startY = cy - 1
startX = cx
for depth in range(1, n // 2 + 1):
    l = 2 * depth + 1
    # 위
    for i in range(l - 1):


    # 오른

    # 아래

    # 왼
