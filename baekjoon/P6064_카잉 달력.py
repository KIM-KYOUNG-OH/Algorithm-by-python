import sys


def solve(m, n, x, y):
    while x <= (m * n):
        if (x - y) % n == 0:
            return x
        x += m
    return -1


t = int(sys.stdin.readline().rstrip())
for _ in range(t):
    M, N, X, Y = map(int, sys.stdin.readline().rstrip().split())
    print(solve(M, N, X, Y))
