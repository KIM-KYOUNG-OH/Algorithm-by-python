import sys

n = int(sys.stdin.readline().rstrip())
dp = []
s = 'SK'
c = 'CY'
dp = [c, s, c, s, s, s, s]
if n < 7:
    print(dp[n])
else:
    tmp = (n - 7) % 7
    print(dp[tmp])
