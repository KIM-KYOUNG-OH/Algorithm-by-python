import sys

n = int(sys.stdin.readline().rstrip())
numbers = list(map(int, sys.stdin.readline().rstrip().split()))
dp = [0 for _ in range(n)]
dp[0] = 1
for i in range(1, n):
    temp = []
    for j in range(i):
        if numbers[j] < numbers[i]:
            temp.append(dp[j] + 1)
    if not temp:
        dp[i] = 1
    else:
        dp[i] = max(temp)
print(max(dp))
