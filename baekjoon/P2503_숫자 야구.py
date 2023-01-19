import sys
from itertools import permutations


def isPossible(questions, cur):
    for num, strike, ball in questions:
        s, b = 0, 0
        for i in range(3):
            if num[i] == cur[i]:
                s += 1
            elif num[i] in cur:
                b += 1
        if strike != s or ball != b:
            return False
    return True


n = int(sys.stdin.readline().rstrip())
questions = []
for _ in range(n):
    num, strike, ball = sys.stdin.readline().rstrip().split()
    strike = int(strike)
    ball = int(ball)
    if strike == 3:
        print(1)
        exit(0)
    questions.append([num, strike, ball])

nums = [i for i in range(1, 10)]
candidates = permutations(map(str, nums), 3)
answer = 0
for candidate in candidates:
    cur = ''.join(candidate)
    if isPossible(questions, cur):
        answer += 1
print(answer)