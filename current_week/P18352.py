from collections import deque


def bfs(start):
    q = deque([(0, start)])
    visited[start] = True
    while q:
        cost, node = q.popleft()
        for next in graph[node]:
            if not visited[next]:
                if cost == k-1:
                    ans.append(next)
                visited[next] = True
                q.append((cost+1, next))


n, m, k, x = map(int, input().split())
graph = [[] for _ in range(n+1)]
visited = [False] * (n + 1)
ans = []
for _ in range(m):
    a, b = map(int, input().split())
    graph[a].append(b)
bfs(x)
if len(ans) == 0:
    print(-1)
else:
    for data in sorted(ans):
        print(data)