import sys


def check_color(y, x, length):
    color = matrix[y][x]
    for i in range(y, y + length):
        for j in range(x, x + length):
            if matrix[i][j] != color:
                return False
    return True


def solution(y, x, length):
    global white, blue
    color = matrix[y][x]
    if check_color(y, x, length):
        if color == 0:
            white += 1
        elif color == 1:
            blue += 1
        return
    solution(y, x, length // 2)
    solution(y + length // 2, x, length // 2)
    solution(y, x + length // 2, length // 2)
    solution(y + length // 2, x + length // 2, length // 2)


n = int(sys.stdin.readline().rstrip())
matrix = []
white, blue = 0, 0
for _ in range(n):
    matrix.append(list(map(int, sys.stdin.readline().rstrip().split())))
solution(0, 0, n)
print(white)
print(blue)
