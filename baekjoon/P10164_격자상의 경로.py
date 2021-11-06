import sys

n, m, k = map(int, sys.stdin.readline().rstrip().split())
dp = [[0] * (m + 1) for _ in range(n + 1)]
for i in range(1, n + 1):
    for j in range(1, m + 1):
        if i == 1 and j == 1:
            dp[i][j] = 1
            continue
        dp[i][j] = dp[i - 1][j] + dp[i][j - 1]
if k == 0:
    print(dp[n][m])
    exit(0)
k_r = (k - 1) // m + 1
k_c = k % m
left_rec_height = k_r
left_rec_width = k_c
right_rec_height = n - k_r + 1
right_rec_width = m - k_c + 1
print(dp[left_rec_height][left_rec_width] * dp[right_rec_height][right_rec_width])
