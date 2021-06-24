import sys


def euclidean(a, b):
    if b == 0:
        return a
    return euclidean(b, a % b)


n = int(sys.stdin.readline().rstrip())
radius = list(map(int, sys.stdin.readline().rstrip().split()))
first_ring = radius[0]
for i in range(1, len(radius)):
    gcd = euclidean(max(first_ring, radius[i]), min(first_ring, radius[i]))
    print(str(first_ring // gcd) + '/' + str(radius[i] // gcd))
