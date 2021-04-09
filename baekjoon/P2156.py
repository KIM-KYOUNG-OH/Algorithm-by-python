import sys
input = sys.stdin.readline

n = int(input())
amount = [0]
for _ in range(n):
    amount.append(int(input()))
dp = [0]*(n+1)
dp[1] = amount[1]
if n>1:
    dp[2] = amount[1]+amount[2]
if n>2:
    dp[3] = max(amount[1]+amount[3], amount[2]+amount[3], dp[2])
for i in range(4, n+1):
    dp[i] = max(dp[i-2]+amount[i], dp[i-3]+amount[i-1]+amount[i], dp[i-1])
print(dp[n])