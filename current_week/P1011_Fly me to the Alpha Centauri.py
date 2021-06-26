import sys

t = int(sys.stdin.readline().rstrip())
for _ in range(t):
    x, y = map(int, sys.stdin.readline().rstrip().split())
    cnt = 0
    distance = y - x
    n = 0
    while True:
        n += 1
        if distance <= (n * (n + 1)):
            diff = n * (n + 1) - distance
            if diff < n:
                cnt = 2 * n
            else:
                cnt = (2 * n) - 1
            break
    print(cnt)
