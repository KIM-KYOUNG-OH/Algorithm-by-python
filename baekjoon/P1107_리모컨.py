import sys

n = int(sys.stdin.readline().rstrip())
m = int(sys.stdin.readline().rstrip())
prohibits = list(map(int, sys.stdin.readline().rstrip().split()))
answer = abs(n - 100)

for i in range(1000001):
    s = str(i)

    for j in range(len(s)):
        if int(s[j]) in prohibits:
            break
        elif j == len(s) - 1:
            answer = min(answer, len(s) + abs(int(i) - n))
print(answer)
