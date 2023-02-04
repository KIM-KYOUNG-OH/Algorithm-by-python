import sys
from collections import deque


def bfs(n, start):
    q = deque()
    q.append(start)
    visit = [False] * (n + 1)
    visit[start] = True
    elements = []
    while q:
        cur = q.popleft()
        elements.append(cur)
        for next in edges[cur]:
            if not visit[next]:
                visit[next] = True
                q.append(next)
    return elements


n = int(sys.stdin.readline().rstrip())
m = int(sys.stdin.readline().rstrip())
edges = [[] for _ in range(n + 1)]
for i in range(1, n + 1):
    tmp = list(map(int, sys.stdin.readline().rstrip().split()))
    for j in range(1, len(tmp) + 1):
        if tmp[j - 1] == 1:
            edges[i].append(j)
path = list(map(int, sys.stdin.readline().rstrip().split()))
start = path[0]
elements = bfs(n, start)
answer = 'YES'
for e in path:
    if e not in elements:
        answer = 'NO'
        break
print(answer)
