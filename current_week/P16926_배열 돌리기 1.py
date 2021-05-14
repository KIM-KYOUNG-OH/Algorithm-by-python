import sys

n, m, r = map(int, sys.stdin.readline().rstrip().split())
matrix = [list(map(int, sys.stdin.readline().rstrip().split())) for _ in range(n)]
for _ in range(r):
    for i in range(min(n, m) // 2):  # 블록 개수
        s_x, s_y = i, i
        s_value = matrix[s_x][s_y]

        for j in range(i+1, n-i):  # 좌
            s_x = j
            prev_value = matrix[s_x][s_y]
            matrix[s_x][s_y] = s_value
            s_value = prev_value
        for j in range(i+1, m-i):  # 하
            s_y = j
            prev_value = matrix[s_x][s_y]
            matrix[s_x][s_y] = s_value
            s_value = prev_value
        for j in range(i+1, n-i):  # 우
            s_x = n - j - 1
            prev_value = matrix[s_x][s_y]
            matrix[s_x][s_y] = s_value
            s_value = prev_value
        for j in range(i+1, m-i):  # 상
            s_y = m - j - 1
            prev_value = matrix[s_x][s_y]
            matrix[s_x][s_y] = s_value
            s_value = prev_value

for i in range(n):
    for j in range(m):
        print(matrix[i][j], end=' ')
    print()