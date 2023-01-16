import sys


def isComplete(startY, startX, endY, endX):
    order = matrix[startY][startX]
    for i in range(startY, endY + 1):
        for j in range(startX, endX + 1):
            if matrix[i][j] != order:
                return False
    return True


def dfs(startY, startX, endY, endX, n):
    if isComplete(startY, startX, endY, endX):
        return matrix[startY][startX]

    area1 = dfs(startY, startX, endY - n // 2, endX - n // 2, n // 2)
    area2 = dfs(startY, startX + n // 2, endY - n // 2, endX, n // 2)
    area3 = dfs(startY + n // 2, startX, endY, endX - n // 2, n // 2)
    area4 = dfs(startY + n // 2, startX + n // 2, endY, endX, n // 2)
    return '(' + area1 + area2 + area3 + area4 + ')'


n = int(sys.stdin.readline().rstrip())
matrix = []
for _ in range(n):
    matrix.append(sys.stdin.readline().rstrip())
answer = dfs(0, 0, n - 1, n - 1, n)
print(answer)