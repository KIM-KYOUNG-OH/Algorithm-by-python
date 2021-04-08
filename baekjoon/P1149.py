n = int(input())
matrix = [[i for i in list(map(int, input().split()))] for _ in range(n)]
dp = [[-1]*3 for _ in range(n)]
dp[0][0] = matrix[0][0]
dp[0][1] = matrix[0][1]
dp[0][2] = matrix[0][2]
for i in range(1, n):
    dp[i][0] = matrix[i][0] + min(dp[i - 1][1], dp[i - 1][2])
    dp[i][1] = matrix[i][1] + min(dp[i - 1][0], dp[i - 1][2])
    dp[i][2] = matrix[i][2] + min(dp[i - 1][0], dp[i - 1][1])
print(min(dp[n-1][0], dp[n-1][1], dp[n-1][2]))