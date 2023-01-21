import sys

n = int(sys.stdin.readline().rstrip())
target = int(sys.stdin.readline().rstrip())
matrix = [[0] * (n + 1) for _ in range(n + 1)]
cy, cx = n // 2 + 1, n // 2 + 1
num = 1
matrix[cy][cx] = num
y = cy - 1
x = cx
answer = [cy, cx]
for depth in range(1, n // 2 + 1):
    l = 2 * depth + 1
    # 위
    for _ in range(l - 2):
        num += 1
        matrix[y][x] = num
        if num == target:
            answer = [y, x]
        x += 1

    # 오른
    for _ in range(l - 1):
        num += 1
        matrix[y][x] = num
        if num == target:
            answer = [y, x]
        y += 1

    # 아래
    for _ in range(l - 1):
        num += 1
        matrix[y][x] = num
        if num == target:
            answer = [y, x]
        x -= 1

    # 왼
    for _ in range(l):
        num += 1
        matrix[y][x] = num
        if num == target:
            answer = [y, x]
        y -= 1

    # for i in range(1, n + 1):
    #     for j in range(1, n + 1):
    #         print(matrix[i][j], end=' ')
    #     print()


for i in range(1, n + 1):
    for j in range(1, n + 1):
        print(matrix[i][j], end=' ')
    print()
print(answer[0], answer[1])
