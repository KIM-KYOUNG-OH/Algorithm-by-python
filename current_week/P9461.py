n = int(input())
request = []
for _ in range(n):
    request.append(int(input()))
m = max(request)
dp = [0] * (m+1)
dp[1] = 1
if m > 1:
    dp[2] = 1
if m > 2:
    dp[3] = 1
if m > 3:
    dp[4] = 2
if m > 4:
    dp[5] = 2
for i in range(6, m+1):
    dp[i] = dp[i-1] + dp[i-5]
for i in request:
    print(dp[i])