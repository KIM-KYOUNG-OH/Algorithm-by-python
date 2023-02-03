import sys
from collections import deque, defaultdict

n, m, r = map(int, sys.stdin.readline().rstrip().split())
graph = [[] for _ in range(n + 1)]
for _ in range(m):
    u, v = map(int, sys.stdin.readline().rstrip().split())
    graph[u].append(v)
    graph[v].append(u)

for i in range(1, n + 1):
    graph[i] = sorted(graph[i])

path = []
q = deque()
q.append(r)
visit = [False] * (n + 1)
visit[r] = True
while q:
    cur = q.popleft()
    path.append(cur)
    for next in graph[cur]:
        if not visit[next]:
            visit[next] = True
            q.append(next)

# print(path)
idx = 1
rank = defaultdict(int)
for e in path:
    rank[e] = idx
    idx += 1

for i in range(1, n + 1):
    print(rank[i])