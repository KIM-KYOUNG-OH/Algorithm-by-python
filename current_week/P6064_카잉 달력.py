import sys

t = int(sys.stdin.readline().rstrip())
for _ in range(t):
    m, n, x, y = map(int, sys.stdin.readline().rstrip().split())
    k, nx, ny = 0, 0, 0
    while True:
        k += 1
        nx += 1
        ny += 1
        if nx > m:
            nx = 1
        if ny > n:
            ny = 1
        if nx == x and ny == y:
            break
        if nx == m and ny == n:
            k = -1
            break
    print(k)
