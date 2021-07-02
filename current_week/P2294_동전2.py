import sys

n, k = map(int, sys.stdin.readline().rstrip().split())
coins = []
for _ in range(n):
    coins.append(int(sys.stdin.readline().rstrip()))
dp = [-1] * (k + 1)
dp[0] = 0
for i in range(1, k + 1):
    for j in range(n):
        if coins[j] <= i and dp[i - coins[j]] != -1:
            if dp[i] == -1:
                dp[i] = dp[i - coins[j]] + 1
            elif dp[i] != -1:
                dp[i] = min(dp[i], dp[i - coins[j]] + 1)
print(dp[-1])
