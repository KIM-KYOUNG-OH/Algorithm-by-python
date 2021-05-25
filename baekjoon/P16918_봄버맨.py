import sys
from collections import deque


def check_bombs():
    for i in range(R):
        for j in range(C):
            if matrix[i][j] == 'O':
                bombs.append((i, j))


def make_bombs():
    for i in range(R):
        for j in range(C):
            if matrix[i][j] == '.':
                matrix[i][j] = 'O'


def explode():
    while bombs:
        r, c = bombs.popleft()
        matrix[r][c] = '.'
        if 0 <= r - 1:
            matrix[r - 1][c] = '.'
        if r + 1 < R:
            matrix[r + 1][c] = '.'
        if 0 <= c - 1:
            matrix[r][c - 1] = '.'
        if c + 1 < C:
            matrix[r][c + 1] = '.'


R, C, N = map(int, sys.stdin.readline().rstrip().split())
matrix = [list(sys.stdin.readline().rstrip()) for _ in range(R)]
N -= 1
while N:
    bombs = deque()
    check_bombs()
    make_bombs()
    N -= 1
    if N == 0:
        break
    explode()
    N -= 1
for i in matrix:
    print(''.join(i))