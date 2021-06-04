# import sys
#
# n, m = map(int, sys.stdin.readline().rstrip().split())
# numbers = list(map(int, sys.stdin.readline().rstrip().split()))
# for _ in range(m):
#     result = 0
#     start, end = map(int, sys.stdin.readline().rstrip().split())
#     for i in range(start - 1, end):
#         result += numbers[i]
#     print(result)

import sys

n, m = map(int, sys.stdin.readline().rstrip().split())
numbers = list(map(int, sys.stdin.readline().rstrip().split()))
memoization = [0] * n  # 누적 합의 값을 미리 구해놓는다
for i in range(n):
    if i == 0:
        memoization[i] = numbers[i]
        continue
    if i != 0:
        memoization[i] = memoization[i - 1] + numbers[i]
for _ in range(m):
    start, end = map(int, sys.stdin.readline().rstrip().split())
    result = memoization[end - 1] - memoization[start - 1] + numbers[start - 1]
    print(result)

