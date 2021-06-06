import sys

n = int(sys.stdin.readline().rstrip())
matrix = []
for _ in range(n):
    matrix.append(list(map(int, sys.stdin.readline().rstrip().split())))
dp = [[0] * n for _ in range(n)]
dp[0][0] = 1
for y in range(n):
    for x in range(n):
        if matrix[y][x] == 0:
            break
        yy = y + matrix[y][x]
        xx = x + matrix[y][x]
        if 0 <= yy < n:
            dp[yy][x] += dp[y][x]
        if 0 <= xx < n:
            dp[y][xx] += dp[y][x]
print(dp[n-1][n-1])