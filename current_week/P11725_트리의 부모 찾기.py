import sys
from collections import deque


def bfs():
    global answer
    q = deque([1])
    visited = [False] * (n + 1)
    visited[1] = True
    while q:
        number = q.popleft()
        for i in matrix[number]:
            if not visited[i]:
                answer[i] = number
                q.append(i)
                visited[i] = True


n = int(sys.stdin.readline().rstrip())
matrix = [[] for _ in range(n + 1)]
answer = dict()
for _ in range(n - 1):
    a, b = map(int, sys.stdin.readline().rstrip().split())
    matrix[a].append(b)
    matrix[b].append(a)
bfs()
for i in range(2, n + 1):
    print(answer[i])
