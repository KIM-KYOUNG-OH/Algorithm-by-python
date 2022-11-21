def solution(n):
    matrix = [[0 for _ in range(n)] for _ in range(n)]
    if n == 1:
        return [1]
    num = 1
    for i in range(n):
        matrix[i][0] = num
        num += 1

    dy = [0, -1, 1]
    dx = [1, -1, 0]
    dir = 0
    y = n - 1
    x = 0
    for k in range(n - 1, 0, -1):
        for _ in range(k):
            y = y + dy[dir]
            x = x + dx[dir]
            matrix[y][x] = num
            num += 1
        dir = (dir + 1) % 3

    answer = []
    for i in range(n):
        for j in range(i + 1):
            answer.append(matrix[i][j])

    return answer


solution(4)