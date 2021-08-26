import sys

n = int(sys.stdin.readline().rstrip())
numbers = list(set(list(map(int, sys.stdin.readline().rstrip().split()))))
numbers.sort()
print(' '.join(map(str, numbers)))