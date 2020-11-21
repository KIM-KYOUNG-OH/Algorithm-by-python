import sys

sys.setrecursionlimit(10000)

t = int(input())
dx, dy = [-1, 1, 0, 0], [0, 0, 1, -1]


def dfs(x, y):
    global matrix, visit
    if visit[x][y] == 1:
        return
    visit[x][y] = 1
    for i in range(4):
        xx = x + dx[i]
        yy = y + dy[i]
        if matrix[xx][yy] == 0 or visit[xx][yy] == 1:
            continue
        dfs(xx, yy)


def process():
    global matrix, visit
    m, n, k = map(int, input().split())
    matrix = [[0 for i in range(m + 2)] for _ in range(n + 2)]
    visit = [[0 for i in range(m + 2)] for _ in range(n + 2)]
    for _ in range(k):
        a, b = map(int, input().split())
        matrix[b + 1][a + 1] = 1
    ans = 0
    for i in range(1, n + 1):
        for j in range(1, m + 1):
            if matrix[i][j] == 0 or visit[i][j] == 1:
                continue
            dfs(i, j)
            ans += 1
    print(ans)


for _ in range(t):
    matrix, visit = [], []
    process()
