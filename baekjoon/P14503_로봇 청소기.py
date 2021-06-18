import sys


def clean(r, c, d):
    global clean_cnt, matrix
    if matrix[r][c] == 0:
        clean_cnt += 1
        matrix[r][c] = 2
    for _ in range(4):
        nd = (d + 3) % 4
        nr = r + dy[nd]
        nc = c + dx[nd]
        if 0 <= nr < n and 0 <= nc < m:
            if matrix[nr][nc] == 0:
                clean(nr, nc, nd)
                return
        d = nd
    nd = (d + 2) % 4
    nr = r + dy[nd]
    nc = c + dx[nd]
    if matrix[nr][nc] == 1:
        return
    clean(nr, nc, d)


n, m = map(int, sys.stdin.readline().rstrip().split())
s_r, s_c, s_d = map(int, sys.stdin.readline().rstrip().split())
matrix = []
for _ in range(n):
    matrix.append(list(map(int, sys.stdin.readline().rstrip().split())))
clean_cnt = 0

dy = [-1, 0, 1, 0]  # 북, 동, 남, 서
dx = [0, 1, 0, -1]

clean(s_r, s_c, s_d)
print(clean_cnt)
