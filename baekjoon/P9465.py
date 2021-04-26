t = int(input())
for _ in range(t):
    n = int(input())
    matrix = []
    dp = [0] * n
    for _ in range(2):
        matrix.append(list(map(int, input().split())))
    dp[0] = (matrix[0][0], matrix[1][0])  # (up, down)
    if n > 1:
        dp[1] = (matrix[0][1] + dp[0][1], matrix[1][1] + dp[0][0])
    for i in range(2, n):
        up = max(dp[i - 1][1] + matrix[0][i], max(dp[i - 2][0], dp[i - 2][1]) + matrix[0][i])
        down = max(dp[i - 1][0] + matrix[1][i], max(dp[i - 2][0], dp[i - 2][1]) + matrix[1][i])
        dp[i] = (up, down)
    print(max(dp[n - 1][0], dp[n - 1][1]))
