import sys

n, m = map(int, sys.stdin.readline().rstrip().split())
numbers = list(map(int, sys.stdin.readline().rstrip().split()))
answer = 0
for i in range(n):
    total = 0
    j = i
    while j < n:
        total += numbers[j]
        if total > m:
            break
        if total == m:
            answer += 1
            break
        j += 1
print(answer)