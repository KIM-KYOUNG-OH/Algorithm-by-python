import sys

n, k = map(int, sys.stdin.readline().rstrip().split())
lst = list(map(int, sys.stdin.readline().rstrip().split()))
result = []
tmp = 0
for i in range(k):
    tmp += lst[i]
result.append(tmp)
for i in range(k, n):
    cumulated_sum = result[-1] - lst[i - k] + lst[i]
    result.append(cumulated_sum)
    print(result)

print(max(result))

