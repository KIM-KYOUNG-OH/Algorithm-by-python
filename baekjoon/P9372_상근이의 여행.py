import sys
from collections import deque


def bfs(x):
    q = deque([x])
    visited[x] = True
    cnt = 0
    while q:
        current = q.popleft()
        for nx in path[current]:
            if not visited[nx]:
                visited[nx] = True
                cnt += 1
                q.append(nx)
    return cnt


t = int(sys.stdin.readline().rstrip())
for _ in range(t):
    n, m = map(int, sys.stdin.readline().rstrip().split())
    path = dict()
    for i in range(1, n + 1):
        path[i] = []
    for _ in range(m):
        a, b = map(int, sys.stdin.readline().rstrip().split())
        path[a].append(b)
        path[b].append(a)
    answer = 0
    visited = [False for _ in range(n + 1)]
    for i in range(1, n + 1):
        if not visited[i]:
            answer += bfs(i)
    print(answer)