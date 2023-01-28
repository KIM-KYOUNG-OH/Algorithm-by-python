import sys

n, k = map(int, sys.stdin.readline().rstrip().split())
r, c = k, n
if k < 2:
    r = 2
if n < 2:
    c = 2
matrix = [[1] * (c + 1) for _ in range(r + 1)]
for j in range(c + 1):
    matrix[0][j] = 0
for i in range(1, r + 1):
    for j in range(1, c + 1):
        matrix[i][j] = matrix[i - 1][j] + matrix[i][j - 1]
print(matrix[k][n] % (10 ** 9))
