import sys
from collections import deque

n = int(sys.stdin.readline().rstrip())
matrix = [[] for _ in range(n)]
for i in range(n):
    tmp = list(map(int, sys.stdin.readline().rstrip().split()))
    matrix[i] = tmp

answer = [[0] * n for _ in range(n)]
for i in range(n):
    # print('i = ', i)
    q = deque()
    q.append(i)
    visited = [False] * n
    while q:
        cur = q.popleft()
        for j in range(n):
            if matrix[cur][j] == 1:
                if not visited[j]:
                    # print('j = ', j)
                    visited[j] = True
                    answer[i][j] = 1
                    q.append(j)
    # print()

for i in range(n):
    for j in range(n):
        print(answer[i][j], end=' ')
    print()
