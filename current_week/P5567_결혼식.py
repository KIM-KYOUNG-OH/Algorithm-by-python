from collections import deque

n = int(input())
m = int(input())
graph = [[] for _ in range(n+1)]
visited = [False] * (n+1)
for _ in range(m):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)
answer = set()
# (depth, node)
q = deque([(0, 1)])
visited[1] = True
while q:
    depth, node = q.popleft()
    if depth == 2:
        break
    for i in graph[node]:
        temp = depth
        if not visited[i]:
            temp += 1
            answer.add(i)
            visited[i] = True
            q.append((temp, i))
print(len(answer))