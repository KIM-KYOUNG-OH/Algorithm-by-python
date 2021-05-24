import sys
from collections import deque


n, m = map(int, sys.stdin.readline().rstrip().split())
numbers = list(map(int, sys.stdin.readline().rstrip().split()))
q = deque([i for i in range(1, n+1)])
cnt = 0
for num in numbers:
    i = 0
    while num != q[i]:
        i += 1
    i = -i if i <= len(q) - i else len(q) - i
    q.rotate(i)
    cnt += abs(i)
    q.popleft()
print(cnt)
