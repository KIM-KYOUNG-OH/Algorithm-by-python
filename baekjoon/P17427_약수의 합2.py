import sys

n = int(sys.stdin.readline().rstrip())
answer = 0
for i in range(1, n + 1):
    answer += (n // i) * i
print(answer)
