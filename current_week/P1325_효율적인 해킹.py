import sys
from collections import deque


def bfs(start):
    q = deque([start])
    visited = [False] * (n + 1)
    visited[start] = True
    hacking_cnt = 1
    while q:
        com = q.popleft()
        for i in graph[com]:
            if not visited[i]:
                q.append(i)
                visited[i] = True
                hacking_cnt += 1
    return hacking_cnt


n, m = map(int, sys.stdin.readline().rstrip().split())
graph = [[] for _ in range(n + 1)]
for _ in range(m):
    A, B = map(int, sys.stdin.readline().rstrip().split())
    graph[B].append(A)

answer = []
max_cnt = 1
for i in range(1, n + 1):
    cnt = bfs(i)
    if max_cnt < cnt:
        answer = [i]
        max_cnt = cnt
    elif max_cnt == cnt:
        answer.append(i)
answer.sort()
print(' '.join(map(str, answer)))
