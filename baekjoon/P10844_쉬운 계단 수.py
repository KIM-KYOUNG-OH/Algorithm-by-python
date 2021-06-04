import sys

n = int(sys.stdin.readline().rstrip())
# dp = [[1 for _ in range(10)]]
# for _ in range(99):
#     dp.append([0 for _ in range(10)])
# for i in range(1, n + 1):
#     for j in range(10):
#         if j <= 8:
#             dp[i][j] += dp[i-1][j+1]
#         if j >= 1:
#             dp[i][j] += dp[i-1][j-1]
# print((sum(dp[n - 1])-dp[n - 1][0]) % int(1e9))

dp = [[0 for _ in range(10)] for _ in range(n + 1)]
for i in range(1, 10):
    dp[1][i] = 1

for i in range(2, n + 1):
    for j in range(10):
        if j == 0:
            dp[i][j] = dp[i-1][j+1] % int(1e9)
        elif j == 9:
            dp[i][j] = dp[i-1][j-1] % int(1e9)
        else:
            dp[i][j] = (dp[i-1][j-1] + dp[i-1][j+1]) % int(1e9)
print(sum(dp[n]) % int(1e9))