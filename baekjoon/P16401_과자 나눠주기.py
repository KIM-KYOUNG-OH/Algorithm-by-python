import sys


def get_cnt(snacks, target):
    cnt = 0
    for snack in snacks:
        cnt += snack // target
    return cnt


m, n = map(int, sys.stdin.readline().rstrip().split())
snacks = list(map(int, sys.stdin.readline().rstrip().split()))
snacks = sorted(snacks)
left = 1
right = max(snacks)
answer = 0
while left <= right:
    mid = (left + right) // 2
    cnt = get_cnt(snacks, mid)
    # print('left = ', left, ', right = ', right, ', mid = ', mid)
    # print('cnt = ', cnt)
    if cnt >= m:
        left = mid + 1
        answer = max(answer, mid)
    else:
        right = mid - 1
print(answer)
