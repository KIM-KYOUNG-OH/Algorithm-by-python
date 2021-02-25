from sys import stdin
from collections import deque


def bfs(result, visit, n, k):
    q = deque()
    q.append(n)
    visit[n] = True
    while q:
        i = q.popleft()
        if i == k:
            return result[i]
        for j in (i+1, i-1, i*2):
            if 0 <= j < 100001 and visit[j] == False:
                visit[j] = True
                q.append(j)
                result[j] = result[i] + 1


n, k = map(int, stdin.readline().split())
visit = [False] * 100001
result = [0] * 100001
print(bfs(result, visit, n, k))
