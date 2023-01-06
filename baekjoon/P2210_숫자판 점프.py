import sys

dy = [-1, 0, 1, 0]
dx = [0, 1, 0, -1]
graph = []
for _ in range(5):
    tmp = list(map(int, sys.stdin.readline().rstrip().split()))
    graph.append(tmp)

history = set()


def dfs(y, x, cur):
    if len(cur) == 6:
        history.add(cur)
        return

    for k in range(4):
        ny = y + dy[k]
        nx = x + dx[k]
        if 0 <= ny < 5 and 0 <= nx < 5:
            dfs(ny, nx, cur + str(graph[ny][nx]))


for i in range(5):
    for j in range(5):
        dfs(i, j, '')
print(len(history))