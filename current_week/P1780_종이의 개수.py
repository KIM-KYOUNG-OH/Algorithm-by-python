import sys


def nine_split(y, x, length):
    global minus, zero, plus

    type_num = matrix[y][x]
    for i in range(y, y + length):
        for j in range(x, x + length):
            if matrix[i][j] != type_num:
                for k in range(3):
                    for l in range(3):
                        nine_split(y + k * (length // 3), x + l * (length // 3), length // 3)
                return
    if type_num == -1:
        minus += 1
    elif type_num == 0:
        zero += 1
    else:
        plus += 1


n = int(sys.stdin.readline().rstrip())
matrix = [list(map(int, sys.stdin.readline().rstrip().split())) for _ in range(n)]
minus = 0
zero = 0
plus = 0
nine_split(0, 0, n)
print(minus)
print(zero)
print(plus)
