import sys
from collections import deque, defaultdict
sys.setrecursionlimit(10**9)


def dfs(n, cur):
    path.append(cur)

    for node in graph[cur]:
        if not visit[node]:
            visit[node] = True
            dfs(n, node)


n, m, r = map(int, sys.stdin.readline().rstrip().split())
graph = [[] for _ in range(n + 1)]
for _ in range(m):
    u, v = map(int, sys.stdin.readline().rstrip().split())
    graph[u].append(v)
    graph[v].append(u)
for i in range(1, n + 1):
    graph[i] = sorted(graph[i])

# for i in range(1, n + 1):
#     print(graph[i])

path = deque()
visit = [False] * (n + 1)
visit[r] = True
dfs(n, r)

answer = defaultdict(int)
idx = 1
while path:
    cur = path.popleft()
    answer[cur] = idx
    idx += 1

for i in range(1, n + 1):
    print(answer[i])
