import sys


def power(a, b):
    if b == 1:
        return a % C
    temp = power(a, b // 2)
    if b % 2 == 0:  # 짝수
        return (temp * temp) % C
    else:  # 홀수
        return (temp * temp * a) % C


A, B, C = map(int, sys.stdin.readline().rstrip().split())
print(power(A, B))
