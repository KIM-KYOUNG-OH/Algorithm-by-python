import sys

n, k = map(int, sys.stdin.readline().rstrip().split())
coins = []
dp = [0] * (k + 1)
dp[0] = 1
for _ in range(n):
    coins.append(int(sys.stdin.readline().rstrip()))
for i in coins:
    for j in range(i, k + 1):
        dp[j] += dp[j - i]
print(dp[k])