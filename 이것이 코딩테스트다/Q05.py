n, m = map(int, input().split())
weight = list(map(int, input().split()))
cnt_by_weight = [0] * 11
for i in weight:
    cnt_by_weight[i] += 1
result = 0
for i in range(1, m+1):
    n -= cnt_by_weight[i]
    result += n * cnt_by_weight[i]
print(result)