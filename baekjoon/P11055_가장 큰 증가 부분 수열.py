import sys

n = int(sys.stdin.readline().rstrip())
A = [0]
A.extend(list(map(int, sys.stdin.readline().rstrip().split())))
dp = [0 for i in range(n + 1)]
dp[1] = A[1]
for i in range(2, n + 1):
    s = []
    for j in range(i - 1, -1, -1):
        if A[i] > A[j]:
            s.append(dp[j])
    if not s:
        dp[i] = A[i-1]
    else:
        dp[i] = max(s) + A[i]
print(max(dp))
