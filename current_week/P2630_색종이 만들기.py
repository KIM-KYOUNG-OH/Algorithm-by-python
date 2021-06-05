import sys


def check_color(y, x, length):
    color = matrix[y][x]
    for i in range(y, y + length):
        for j in range(x, x + length):
            if matrix[i][j] != color:
                return False
    return True


def solution(y, x, depth):
    global white, blue
    col = matrix[y][x]
    if check_color(y, x, depth):
        if col == 0:
            white += 1
        elif col == 1:
            blue += 1
        return
    solution(y, x, depth // 2)
    solution(y + depth // 2, x, depth // 2)
    solution(y, x + depth // 2, depth // 2)
    solution(y + depth // 2, x + depth // 2, depth // 2)


n = int(sys.stdin.readline().rstrip())
matrix = []
white, blue = 0, 0
for _ in range(n):
    matrix.append(list(map(int, sys.stdin.readline().rstrip().split())))
solution(0, 0, n)
print(white)
print(blue)
