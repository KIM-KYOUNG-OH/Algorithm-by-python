import sys
from itertools import combinations

l, c = map(int, sys.stdin.readline().rstrip().split())
alps = list(sys.stdin.readline().rstrip().split())
vowels = ['a', 'e', 'i', 'o', 'u']
answer = []

candidates = list(combinations(alps, l))
for candidate in candidates:
    if len(set(vowels) & set(candidate)) >= 1 and len(set(candidate) - set(vowels)) >= 2:  # 최소 한 개의 모음 & 최소 두 개의 자음
        answer.append(''.join(sorted(candidate)))
answer.sort()
for i in answer:
    print(i)