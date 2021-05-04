def rotate_by_clockwise(matrix):
    row = len(matrix)
    col = len(matrix[0])
    result = [[0] * row for _ in range(col)]
    for i in range(row):
        for j in range(col):
            result[j][row - i - 1] = matrix[i][j]
    return result


def is_open(matrix):
    lock_length = len(matrix) // 3
    for i in range(lock_length, lock_length * 2):
        for j in range(lock_length, lock_length * 2):
            if matrix[i][j] != 1:
                return False
    return True


def solution(key, lock):
    n = len(lock)
    m = len(key)
    new_lock = [[0] * (n * 3) for _ in range(3 * n)]
    for i in range(n, 2 * n):
        for j in range(n, 2 * n):
            new_lock[i][j] = lock[i - n][j - n]
    for _ in range(4):
        key = rotate_by_clockwise(key)
        for y in range(2 * n):
            for x in range(2 * n):
                for i in range(m):
                    for j in range(m):
                        new_lock[y + i][x + j] += key[i][j]
                if is_open(new_lock):
                    return True
                for i in range(m):
                    for j in range(m):
                        new_lock[y + i][x + j] -= key[i][j]
    return False
