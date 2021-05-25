import sys
from collections import deque

n, k = map(int, sys.stdin.readline().rstrip().split())
q = deque([])
for i in range(1, n+1):
    q.append(i)
print('<', end='')
while q:
    for _ in range(k):
        num = q.popleft()
        q.append(num)
    print(q.pop(), end='')
    if q:
        print(', ', end='')
print('>')
