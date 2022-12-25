def solution(brown, yellow):
    total = brown + yellow
    r, c = 0, 0
    for col in range(total, 0, -1):
        if total % col != 0:
            continue
        row = total // col
        if row > col:
            break
        b = 2 * (row + col) - 4
        if b == brown:
            r = row
            c = col
            break
    return [c, r]


print(solution(10, 2))
