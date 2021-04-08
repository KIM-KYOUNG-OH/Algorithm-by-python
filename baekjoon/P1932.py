n = int(input())
dp = []
matrix = [[int(input())]]
for i in range(n-1):
    matrix.append(list(map(int, input().split())))
dp = [[matrix[0][0]]]
for i in range(1, n):
    for j in range(i+1):
        if j == 0:
            dp.append([matrix[i][j] + dp[i-1][j]])
        elif 0<j<i:
            dp[i].append(matrix[i][j]+max(dp[i-1][j-1], dp[i-1][j]))
        elif i==j:
            dp[i].append(matrix[i][j]+dp[i-1][j-1])
print(max(dp[-1]))