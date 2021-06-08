import sys
from itertools import combinations


def GCD(A: int, B: int) -> int:
    if B == 0:
        return A
    return GCD(B, A % B)


t = int(sys.stdin.readline().rstrip())
for _ in range(t):
    lst = list(map(int, sys.stdin.readline().rstrip().split()))
    n = lst[0]
    numbers = lst[1:]
    if n == 1:
        continue
    candidates = list(combinations(numbers, 2))
    result = 0
    for candidate in candidates:
        a, b = candidate
        if b > a:
            a, b = b, a
        result += GCD(a, b)
    print(result)
