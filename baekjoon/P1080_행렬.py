import sys


def convert_matrix(r, c, matrix):
    for i in range(r, r + 3):
        for j in range(c, c + 3):
            matrix[i][j] = 1 - matrix[i][j]


n, m = map(int, sys.stdin.readline().rstrip().split())
standard_matrix = []  # 기준 행렬
change_matrix = []  # 수정할 행렬
for _ in range(n):
    standard_matrix.append(list(map(int, list(sys.stdin.readline().rstrip()))))
for _ in range(n):
    change_matrix.append(list(map(int, list(sys.stdin.readline().rstrip()))))
convert_cnt = 0  # 뒤집는 횟수

for i in range(n - 2):
    for j in range(m - 2):
        if standard_matrix[i][j] != change_matrix[i][j]:
            convert_matrix(i, j, change_matrix)
            convert_cnt += 1

for i in range(n):
    for j in range(m):
        if standard_matrix[i][j] != change_matrix[i][j]:
            print(-1)
            exit(0)
print(convert_cnt)