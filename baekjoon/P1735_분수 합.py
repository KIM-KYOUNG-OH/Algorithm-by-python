import sys


def get_GCD(a, b):
    if b == 0:
        return a
    return get_GCD(b, a % b)


child1, mom1 = map(int, sys.stdin.readline().rstrip().split())
child2, mom2 = map(int, sys.stdin.readline().rstrip().split())
gcd = get_GCD(child2 * mom1 + child1 * mom2, mom1 * mom2)
result_child = (child2 * mom1 + child1 * mom2) // gcd
result_mom = (mom1 * mom2) // gcd
print(result_child, result_mom)
