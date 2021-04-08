from collections import deque

def bfs(v):
    global ans
    q = deque([v])
    visited[v] = True
    while q:
        a = q.popleft()
        for i in range(1, n+1):
            if graph[a][i] and not visited[i]:
                ans += 1
                q.append(i)
                visited[i] = True

n = int(input())
graph = [[0 for _ in range(n+1)] for _ in range(n+1)]
visited = [False]*(n+1)
ans = 0
m = int(input())
for _ in range(m):
    a,b = map(int, input().split())
    graph[a][b] = 1
    graph[b][a] = 1
bfs(1)
print(ans)