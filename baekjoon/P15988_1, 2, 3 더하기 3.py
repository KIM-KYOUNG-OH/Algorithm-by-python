import sys

t = int(sys.stdin.readline().rstrip())
dp = [0] * 1000001
dp[0], dp[1], dp[2] = 1, 1, 2
for i in range(3, 1000001):
    dp[i] = (dp[i - 1] + dp[i - 2] + dp[i - 3]) % 1000000009
for _ in range(t):
    n = int(sys.stdin.readline().rstrip())
    print(dp[n])
