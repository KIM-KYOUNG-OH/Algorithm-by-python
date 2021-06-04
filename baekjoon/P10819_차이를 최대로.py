import sys
from itertools import permutations

n = int(sys.stdin.readline().rstrip())
lst = list(map(int, sys.stdin.readline().rstrip().split()))
lst_cases = permutations(lst, n)
answer = 0
for case in list(lst_cases):
    total = 0
    for i in range(n-1):
        total += abs(case[i+1] - case[i])
    answer = max(answer, total)
print(answer)