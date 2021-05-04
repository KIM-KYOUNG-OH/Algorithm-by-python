def virus(s_x, s_y):
    for i in range(4):
        nx = s_x + dx[i]
        ny = s_y + dy[i]
        if 0 <= nx < n and 0 <= ny < m:
            if temp[nx][ny] == 0:
                temp[nx][ny] = 2
                virus(nx, ny)


def get_score():
    score = 0
    for i in range(n):
        for j in range(m):
            if temp[i][j] == 0:
                score += 1
    return score


def dfs(cnt):
    global result
    if cnt == 3:
        for i in range(n):
            for j in range(m):
                temp[i][j] = matrix[i][j]
        for i in range(n):
            for j in range(m):
                if temp[i][j] == 2:
                    virus(i, j)
        result = max(result, get_score())
        return
    for i in range(n):
        for j in range(m):
            if matrix[i][j] == 0:
                matrix[i][j] = 1
                cnt += 1
                dfs(cnt)
                cnt -= 1
                matrix[i][j] = 0


n, m = map(int, input().split())
matrix = []
for _ in range(n):
    matrix.append(list(map(int, input().split())))
temp = [[0] * m for _ in range(n)]  # 벽 친뒤 행렬

dx = [-1, 0, 1, 0]
dy = [0, -1, 0, 1]

result = 0

dfs(0)
print(result)