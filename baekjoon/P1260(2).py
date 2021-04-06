from collections import deque
import heapq


def dfs(v):
    print(v, end=' ')
    dfs_visited[v] = True
    for i in graph[v]:
        if not dfs_visited[i]:
            dfs(i)


def bfs(v):
    queue = deque([v])
    bfs_visited[v] = True
    while queue:
        a = queue.popleft()
        print(a, end=' ')
        for i in graph[a]:
            if not bfs_visited[i]:
                queue.append(i)
                bfs_visited[i] = True


n,m,v = map(int, input().split())
graph = [[] for _ in range(n+1)]
dfs_visited = [False] * (n+1)
bfs_visited = [False] * (n+1)
for _ in range(m):
    a,b = map(int, input().split())
    heapq.heappush(graph[a], b)
    heapq.heappush(graph[b], a)

dfs(v)
print()
bfs(v)