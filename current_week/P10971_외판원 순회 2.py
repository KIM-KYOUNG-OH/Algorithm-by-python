import sys


def dfs(start, next, value, visited):
    global min_value
    if len(visited) == n:
        if matrix[next][start] != 0:
            min_value = min(min_value, value + matrix[next][start])
        return
    for i in range(n):
        if matrix[next][i] != 0 and i not in visited:
            visited.append(i)
            dfs(start, i, value + matrix[next][i], visited)
            visited.pop()


n = int(sys.stdin.readline().rstrip())
matrix = []
min_value = int(1e9)
for _ in range(n):
    matrix.append(list(map(int, sys.stdin.readline().rstrip().split())))
for i in range(n):
    dfs(i, i, 0, [i])
print(min_value)