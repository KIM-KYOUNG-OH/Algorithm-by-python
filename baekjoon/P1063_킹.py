import sys


def parse(y, x):
    alp = chr(x - 1 + ord('A'))
    return alp + str(y)


dy = [0, 0, -1, 1, 1, 1, -1, -1]  # R, L, B, T, RT, LT, RB, LB
dx = [1, -1, 0, 0, 1, -1, 1, -1]
direction = {'R': 0, 'L': 1, 'B': 2, 'T': 3, 'RT': 4, 'LT': 5, 'RB': 6, 'LB': 7}

king, rock, n = sys.stdin.readline().rstrip().split(' ')
n = int(n)
ky = int(king[1])
kx = ord(king[0]) - ord('A') + 1
ry = int(rock[1])
rx = ord(rock[0]) - ord('A') + 1
for _ in range(n):
    prev_ky = ky
    prev_kx = kx
    prev_ry = ry
    prev_rx = rx
    d = sys.stdin.readline().rstrip()
    nky = ky + dy[direction[d]]
    nkx = kx + dx[direction[d]]
    if 0 < nky <= 8 and 0 < nkx <= 8:
        ky, kx = nky, nkx

    if ky == ry and kx == rx:
        nry = ry + dy[direction[d]]
        nrx = rx + dx[direction[d]]
        if 0 < nry <= 8 and 0 < nrx <= 8:
            ry, rx = nry, nrx

    if ky == ry and kx == rx:
        ky, kx = prev_ky, prev_kx
        ry, rx = prev_ry, prev_rx

# print('ky = ', ky, ', kx = ', kx)
# print('ry = ', ry, ', rx = ', rx)
kPos = parse(ky, kx)
rPos = parse(ry, rx)
print(kPos)
print(rPos)