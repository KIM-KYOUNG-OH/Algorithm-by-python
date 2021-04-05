def solution(key, lock):
    def attach(x, y):
        for i in range(m):
            for j in range(m):
                matrix[x+i][y+j] += key[i][j]

    def detach(x, y):
        for i in range(m):
            for j in range(m):
                matrix[x+i][y+j] -= key[i][j]

    def is_open():
        for i in range(n):
            for j in range(n):
                if matrix[m+i][m+j] != 1:
                    return False
        return True

    def rotate():
        return list(zip(*key[::-1]))

    m, n = len(key), len(lock)
    matrix = [[0]*(m*2+n) for _ in range(m*2+n)]
    for i in range(n):
        for j in range(n):
            matrix[m+i][m+j] = lock[i][j]
    for _ in range(4):
        key = rotate()
        for i in range(1, m+n):
            for j in range(1, m+n):
                attach(i, j)
                if is_open():
                    return True
                detach(i, j)

    return False

print(solution([[0, 0, 0], [1, 0, 0], [0, 1, 1]],[[1, 1, 1], [1, 1, 0], [1, 0, 1]]))