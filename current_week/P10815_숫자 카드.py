import sys

n = int(sys.stdin.readline().rstrip())
sanggun = list(map(int, sys.stdin.readline().rstrip().split()))
sanggun_dict = dict()
for num in sanggun:
    sanggun_dict[num] = 1
m = int(sys.stdin.readline().rstrip())
find = list(map(int, sys.stdin.readline().rstrip().split()))
for num in find:
    if num not in sanggun_dict:
        print(0, end=' ')
    else:
        print(1, end=' ')