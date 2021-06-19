import sys
from itertools import permutations

k = int(sys.stdin.readline().rstrip())
brackets = sys.stdin.readline().rstrip().split()
numbers = [i for i in range(10)]
candidates = list(permutations(numbers, k + 1))
answer = []
for candidate in candidates:
    breaker = False
    for i in range(k):
        if brackets[i] == '<':
            if candidate[i] > candidate[i + 1]:
                breaker = True
                break
        elif brackets[i] == '>':
            if candidate[i] < candidate[i + 1]:
                breaker = True
                break
    if breaker:
        continue
    answer.append(''.join(map(str, candidate)))
answer.sort()
print(answer[-1])
print(answer[0])
