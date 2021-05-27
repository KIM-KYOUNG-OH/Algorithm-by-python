import sys

n = int(sys.stdin.readline().rstrip())
numbers = list(map(int, sys.stdin.readline().rstrip().split()))
dp = [1 for _ in range(n)]
for i in range(1, n):
    temp = []
    for j in range(i):
        if numbers[i] < numbers[j]:
            temp.append(dp[j])
    if len(temp) == 0:
        continue
    dp[i] += max(temp)
print(max(dp))