import sys


def get_GCD(a, b):
    if b == 0:
        return a
    return get_GCD(b, a % b)


A, B = map(int, sys.stdin.readline().rstrip().split())
if A < B:
    A, B = B, A
print('1' * get_GCD(A, B))