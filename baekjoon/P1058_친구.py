import sys
from collections import deque


def bfs(n, num):
    q = deque()
    q.append([num, 0])
    visit = [False] * (n + 1)
    visit[num] = True
    cnt = 0
    while q:
        cur, depth = q.popleft()
        if depth > 2:
            continue
        elif 0 < depth <= 2:
            cnt += 1
        for next in graph[cur]:
            if not visit[next]:
                visit[next] = True
                q.append([next, depth + 1])
    return cnt


n = int(sys.stdin.readline().rstrip())
graph = [[] for _ in range(n + 1)]
for i in range(1, n + 1):
    s = sys.stdin.readline().rstrip()
    for j in range(1, n + 1):
        if s[j - 1] == 'Y':
            graph[i].append(j)

max_val = 0
for i in range(1, n + 1):
    cnt = bfs(n, i)
    max_val = max(max_val, cnt)
print(max_val)
