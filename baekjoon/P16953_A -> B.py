import sys
from collections import deque

a, b = map(int, sys.stdin.readline().rstrip().split())
q = deque()
q.append([a, 1])
answer = -1
while q:
    cur, cnt = q.popleft()
    if cur > b:
        continue
    elif cur == b:
        answer = cnt
        break
    q.append([cur * 2, cnt + 1])
    q.append([cur * 10 + 1, cnt + 1])
print(answer)
