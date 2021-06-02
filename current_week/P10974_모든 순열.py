import sys
from itertools import permutations

n = int(sys.stdin.readline().rstrip())
numbers = [i for i in range(1, n+1)]
lst = permutations(numbers, n)
for i in lst:
    print(' '.join(map(str, i)))