import sys

n = int(sys.stdin.readline().rstrip())
nums = list(map(int, sys.stdin.readline().rstrip().split()))
dp = [1001] * n
dp[0] = 0
for i in range(1, n):
    for j in range(i):
        # print('j = ', j)
        if i - j <= nums[j]:
            dp[i] = min(dp[i], dp[j] + 1)
# print(dp)
if dp[-1] == 1001:
    print(-1)
else:
    print(dp[-1])
