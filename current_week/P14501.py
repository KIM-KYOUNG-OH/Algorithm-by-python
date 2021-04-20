n = int(input())
consults = [0] * (n+1)
dp = [0] * (n+6)
for i in range(1, n+1):
    t, p = map(int, input().split())
    consults[i] = (t, p)

for i in range(n, 0, -1):
    cost = consults[i][1] if consults[i][0]+i-1 <= n else 0
    dp[i] = max(cost + dp[i+consults[i][0]], dp[i+1])

print(dp[1])