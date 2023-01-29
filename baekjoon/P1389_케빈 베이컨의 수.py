import sys
from collections import deque

n, m = map(int, sys.stdin.readline().rstrip().split())
graph = [[] for _ in range(n + 1)]
for _ in range(m):
    a, b = map(int, sys.stdin.readline().rstrip().split())
    graph[a].append(b)
    graph[b].append(a)

kavin_bacons = []
for i in range(1, n + 1):
    q = deque()
    q.append([i, 0])
    total = 0
    visit = [False] * (n + 1)
    while q:
        cur, cost = q.popleft()
        total += cost
        for next in graph[cur]:
            if not visit[next]:
                visit[next] = True
                q.append([next, cost + 1])
    kavin_bacons.append([total, i])
kavin_bacons = sorted(kavin_bacons, key=lambda x: (x[0], x[1]))
print(kavin_bacons[0][1])
