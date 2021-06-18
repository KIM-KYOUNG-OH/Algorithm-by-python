import sys
from collections import deque


def count_RGB(graph):
    result = 0
    visited = [[False] * n for _ in range(n)]
    for i in range(n):
        for j in range(n):
            if not visited[i][j]:
                q = deque([(i, j)])
                visited[i][j] = True
                current_color = graph[i][j]
                result += 1
                while q:
                    r, c = q.popleft()
                    for k in range(4):
                        nr = r + dy[k]
                        nc = c + dx[k]
                        if 0 <= nr < n and 0 <= nc < n:
                            if not visited[nr][nc] and graph[nr][nc] == current_color:
                                q.append((nr, nc))
                                visited[nr][nc] = True
    return result


n = int(sys.stdin.readline().rstrip())
matrix = []
for _ in range(n):
    matrix.append(list(sys.stdin.readline().rstrip()))
fixed_matrix = [[] for _ in range(n)]
for i in range(n):
    for j in range(n):
        if matrix[i][j] == 'R' or matrix[i][j] == 'G':
            fixed_matrix[i].append('R')
        else:
            fixed_matrix[i].append('B')

dy = [-1, 0, 1, 0]
dx = [0, -1, 0, 1]

print(count_RGB(matrix), end=' ')
print(count_RGB(fixed_matrix))