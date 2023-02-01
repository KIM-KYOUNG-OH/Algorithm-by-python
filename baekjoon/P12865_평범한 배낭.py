import sys

n, k = map(int, sys.stdin.readline().rstrip().split())
weight = [0]
value = [0]
for _ in range(n):
    w, v = map(int, sys.stdin.readline().rstrip().split())
    weight.append(w)
    value.append(v)

dp = [[0] * (k + 1) for _ in range(n + 1)]
for i in range(1, n + 1):
    for j in range(1, k + 1):
        if j - weight[i] >= 0:
            dp[i][j] = max(dp[i - 1][j], dp[i - 1][j - weight[i]] + value[i])
        else:
            dp[i][j] = dp[i - 1][j]
print(dp[n][k])
