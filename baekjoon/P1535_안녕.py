import sys

n = int(sys.stdin.readline().rstrip())
loss = [0] + list(map(int, sys.stdin.readline().rstrip().split()))
joy = [0] + list(map(int, sys.stdin.readline().rstrip().split()))

dp = [[0] * 101 for _ in range(n + 1)]
for i in range(1, n + 1):
    for j in range(1, 101):
        if loss[i] <= j:
            dp[i][j] = max(dp[i - 1][j], dp[i - 1][j - loss[i]] + joy[i])
        else:
            dp[i][j] = dp[i - 1][j]
print(dp[n][99])
