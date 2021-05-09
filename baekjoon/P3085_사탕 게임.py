from collections import deque


def check_candy():
    for i in range(n):
        for j in range(n):
            right_search(i, j)
            down_search(i, j)


def right_search(start_x, start_y):
    global answer
    q = deque([(start_x, start_y)])
    cnt = 1
    color = matrix[start_x][start_y]
    while q:
        x, y = q.popleft()
        ny = y + 1
        if ny < n:
            if color == matrix[x][ny]:
                cnt += 1
                q.append((x, ny))
    answer = max(answer, cnt)


def down_search(start_x, start_y):
    global answer
    q = deque([(start_x, start_y)])
    cnt = 1
    color = matrix[start_x][start_y]
    while q:
        x, y = q.popleft()
        nx = x + 1
        if nx < n:
            if color == matrix[nx][y]:
                cnt += 1
                q.append((nx, y))
    answer = max(answer, cnt)


n = int(input())
matrix = []
answer = 0
for _ in range(n):
    matrix.append(list(input()))
for i in range(n):
    for j in range(n):
        if j < n-1 and matrix[i][j] != matrix[i][j+1]:
            matrix[i][j], matrix[i][j + 1] = matrix[i][j + 1], matrix[i][j]
            check_candy()
            matrix[i][j], matrix[i][j + 1] = matrix[i][j + 1], matrix[i][j]
        if i < n-1 and matrix[i][j] != matrix[i+1][j]:
            matrix[i][j], matrix[i+1][j] = matrix[i+1][j], matrix[i][j]
            check_candy()
            matrix[i][j], matrix[i + 1][j] = matrix[i + 1][j], matrix[i][j]
print(answer)