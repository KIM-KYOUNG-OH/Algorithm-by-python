import sys

n, m = map(int, sys.stdin.readline().rstrip().split())
matrix = []
for _ in range(n):
    matrix.append(list(map(int, list(sys.stdin.readline().rstrip()))))
length = min(n, m)  # 정사각형의 길이
while length:
    for i in range(n - length + 1):
        for j in range(m - length + 1):
            if (matrix[i][j] == matrix[i][j + length - 1]
                    and matrix[i][j] == matrix[i + length - 1][j]
                    and matrix[i][j] == matrix[i + length - 1][j + length - 1]):
                print(length ** 2)
                exit(0)
    length -= 1
