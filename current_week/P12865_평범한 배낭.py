import sys


# def recursive(idx, total_weight, total_value):
#     global answer
#     if idx >= n:
#         answer = max(answer, total_value)
#         return
#     for i in range(idx, n):
#         if total_weight + stuff[i][0] <= k:
#             recursive(i + 1, total_weight + stuff[i][0], total_value + stuff[i][1])
#     answer = max(answer, total_value)
#     return
n, k = map(int, sys.stdin.readline().rstrip().split())
stuff = [(0, 0)]
for _ in range(1, n + 1):
    w, v = map(int, sys.stdin.readline().rstrip().split())
    stuff.append((w, v))
dp = [[0] * (k + 1) for _ in range(n + 1)]

for i in range(1, n + 1):
    for j in range(1, k + 1):
        if j >= stuff[i][0]:
            dp[i][j] = max(dp[i - 1][j], dp[i - 1][j - stuff[i][0]] + stuff[i][1])
        else:
            dp[i][j] = dp[i - 1][j]
print(dp[-1][-1])