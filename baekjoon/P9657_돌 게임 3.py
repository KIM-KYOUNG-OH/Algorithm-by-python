import sys

n = int(sys.stdin.readline().rstrip())
dp = []
if n < 4:
    dp = [0] * 5
else:
    dp = [0] * (n + 1)
dp[1], dp[2], dp[3], dp[4] = 'SK', 'CY', 'SK', 'SK'
for i in range(5, n + 1):
    a, b, c = dp[i - 1], dp[i - 3], dp[i - 4]
    if a == 'SK' and b == 'SK' and c == 'SK':
        dp[i] = 'CY'
    else:
        dp[i] = 'SK'
print(dp[n])