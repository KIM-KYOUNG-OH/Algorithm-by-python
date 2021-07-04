# import sys
#
# def dfs(r, c, total_candy):
#     global answer
#     if r == (n - 1) and c == (m - 1):
#         answer = max(answer, total_candy)
#         return
#     for i in range(3):
#         nr = r + dr[i]
#         nc = c + dc[i]
#         if 0 <= nr < n and 0 <= nc < m:
#             dfs(nr, nc, total_candy + matrix[nr][nc])
#
#
# n, m = map(int, sys.stdin.readline().rstrip().split())
# matrix = []
# for _ in range(n):
#     matrix.append(list(map(int, sys.stdin.readline().rstrip().split())))
#
# dr = [1, 0, 1]
# dc = [0, 1, 1]
#
# answer = 0
#
# dfs(0, 0, matrix[0][0])

import sys

n, m = map(int, sys.stdin.readline().rstrip().split())
matrix = [[0] * (m + 1) for _ in range(n + 1)]
for i in range(1, n + 1):
    lst = list(map(int, sys.stdin.readline().rstrip().split()))
    for j in range(len(lst)):
        matrix[i][j + 1] = lst[j]
dp = [[0] * (m + 1) for _ in range(n + 1)]

for i in range(n + 1):
    for j in range(m + 1):
        dp[i][j] = max(dp[i - 1][j], dp[i][j - 1]) + matrix[i][j]
print(dp[-1][-1])
