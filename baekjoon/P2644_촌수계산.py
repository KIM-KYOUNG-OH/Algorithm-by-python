import sys
from collections import deque


def bfs(start):
    q = deque([start])
    visited = [False for _ in range(n + 1)]
    visited[start] = True
    while q:
        num = q.popleft()
        for i in matrix[num]:
            if not visited[i]:
                visited[i] = True
                result[i] = result[num] + 1
                q.append(i)


n = int(sys.stdin.readline().rstrip())
a, b = map(int, sys.stdin.readline().rstrip().split())
m = int(sys.stdin.readline().rstrip())
matrix = [[] for _ in range(n + 1)]
result = [0 for _ in range(n + 1)]
for _ in range(m):
    parent, child = map(int, sys.stdin.readline().rstrip().split())
    matrix[parent].append(child)
    matrix[child].append(parent)
bfs(a)
if result[b] != 0:
    print(result[b])
else:
    print(-1)

