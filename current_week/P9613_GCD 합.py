import sys
from itertools import combinations


def GCD(A, B):
    if B == 0:
        return A
    GCD(B, A % B)


t = int(sys.stdin.readline().rstrip())
for _ in range(t):
    lst = list(map(int, sys.stdin.readline().rstrip().split()))
    n = lst[0]
    numbers = lst[1:]
    if n == 1:
        print(numbers[0])
        continue
    candidates = combinations(numbers, 2)
    result = 0
    for candidate in candidates:
        a, b = candidate
        if b > a:
            a, b = b, a
        result += GCD(a, b)
    print(result)
