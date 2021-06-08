import sys


def binary_search(left, right):
    result = 0  # 최대 예산 합
    limit = 0  # 최대 상한액
    while left <= right:
        mid = (left + right) // 2
        total = 0
        for money in moneys:
            if money > mid:
                total += mid
                continue
            total += money
        if total <= m:
            if result <= total:
                result = total
                limit = mid
            left = mid + 1
            continue
        if total > m:
            right = mid - 1
    return limit


n = int(sys.stdin.readline().rstrip())
moneys = list(map(int, sys.stdin.readline().rstrip().split()))
m = int(sys.stdin.readline().rstrip())
print(binary_search(0, max(moneys)))