import sys

n, m = map(int, sys.stdin.readline().rstrip().split())
s = dict()
for _ in range(n):
    tmp = sys.stdin.readline().rstrip()
    s[tmp] = 0

answer = 0
for _ in range(m):
    tmp = sys.stdin.readline().rstrip()
    if tmp in s.keys():
        answer += 1
print(answer)