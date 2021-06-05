import sys
from collections import deque

n = int(sys.stdin.readline().rstrip())
q = deque([])
for _ in range(n):
    order = list(sys.stdin.readline().rstrip().split())
    if order[0] == 'push':
        q.append(int(order[1]))
    elif order[0] == 'pop':
        if len(q):
            print(q.popleft())
        else:
            print(-1)
    elif order[0] == 'size':
        print(len(q))
    elif order[0] == 'empty':
        if len(q):
            print(0)
        else:
            print(1)
    elif order[0] == 'front':
        if q:
            print(q[0])
        else:
            print(-1)
    elif order[0] == 'back':
        if q:
            print(q[-1])
        else:
            print(-1)