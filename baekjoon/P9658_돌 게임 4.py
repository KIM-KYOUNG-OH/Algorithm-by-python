import sys

n = int(sys.stdin.readline().rstrip())
dp = []
if n < 4:
    dp = [''] * 5
else:
    dp = [''] * (n + 1)
dp[1], dp[2], dp[3], dp[4] = 'CY', 'SK', 'CY', 'SK'
for i in range(5, n + 1):
    a, b, c = dp[i - 1], dp[i - 3], dp[i - 4]
    if a == 'CY' or b == 'CY' or c == 'CY':
        dp[i] = 'SK'
    else:
        dp[i] = 'CY'
print(dp[n])