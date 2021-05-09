import sys


def dfs(idx, ans):
    global max_result, min_result
    if idx == n:
        min_result = min(min_result, ans)
        max_result = max(max_result, ans)
        return
    if operator_cnt[0] > 0:
        operator_cnt[0] -= 1
        dfs(idx + 1, ans + numbers[idx])
        operator_cnt[0] += 1
    if operator_cnt[1] > 0:
        operator_cnt[1] -= 1
        dfs(idx + 1, ans - numbers[idx])
        operator_cnt[1] += 1
    if operator_cnt[2] > 0:
        operator_cnt[2] -= 1
        dfs(idx + 1, ans * numbers[idx])
        operator_cnt[2] += 1
    if operator_cnt[3] > 0:
        operator_cnt[3] -= 1
        dfs(idx + 1, int(ans / numbers[idx]))
        operator_cnt[3] += 1


n = int(input())
numbers = list(map(int, sys.stdin.readline().rstrip().split()))
operator_cnt = list(map(int, sys.stdin.readline().rstrip().split()))
max_result = int(1e9) * (-1)
min_result = int(1e9)
dfs(1, numbers[0])
print(max_result)
print(min_result)