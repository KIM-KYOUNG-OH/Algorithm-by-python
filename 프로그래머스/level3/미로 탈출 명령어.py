def solution(n, m, x, y, r, c, k):
    stack = [(x, y, '')]
    result = "impossible"
    while stack:
        yy, xx, path = stack.pop()
        if len(path) == k and (yy, xx) == (r, c):
            result = path
            break
        remain, shortest_path = k - len(path), abs(yy - r) + abs(xx - c)
        if remain < shortest_path or remain % 2 != shortest_path % 2:
            continue
        if yy > 1:
            stack.append((yy - 1, xx, path + 'u'))
        if xx < m:
            stack.append((yy, xx + 1, path + 'r'))
        if xx > 1:
            stack.append((yy, xx - 1, path + 'l'))
        if yy < n:
            stack.append((yy + 1, xx, path + 'd'))
    return result