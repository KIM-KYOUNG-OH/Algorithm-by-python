import sys

n = int(sys.stdin.readline().rstrip())
lst = [0]
numbers = list(map(int, sys.stdin.readline().rstrip().split()))
lst.extend(numbers)
m = int(sys.stdin.readline().rstrip())
cumulated_sum = [0]
for i in range(1, len(lst)):
    cumulated_sum.append(cumulated_sum[i - 1] + lst[i])
for _ in range(m):
    a, b = map(int, sys.stdin.readline().rstrip().split())
    print(cumulated_sum[b] - cumulated_sum[a - 1])
