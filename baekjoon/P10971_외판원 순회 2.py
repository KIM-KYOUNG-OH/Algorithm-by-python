import sys


def dfs(start, current, value, visited):
    global min_value
    if len(visited) == n:
        if matrix[current][start] != 0:
            min_value = min(min_value, value + matrix[current][start])
        return
    for i in range(n):
        if matrix[current][i] != 0 and i not in visited:
            visited.append(i)
            dfs(start, i, value + matrix[current][i], visited)
            visited.pop()


n = int(sys.stdin.readline().rstrip())
matrix = []
min_value = int(1e9)
for _ in range(n):
    matrix.append(list(map(int, sys.stdin.readline().rstrip().split())))
for i in range(n):
    dfs(i, i, 0, [i])
print(min_value)