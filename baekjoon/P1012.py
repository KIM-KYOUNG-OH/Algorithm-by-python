# import sys
#
# sys.setrecursionlimit(10000)
#
# T = int(input())
# dx, dy = [-1, 0, 1, 0], [0, -1, 0, 1]
#
#
# def dfs(x, y):
#     global B, ck
#     if ck[x][y] == 1:
#         return
#     ck[x][y] = 1
#     for i in range(4):
#         xx, yy = x + dx[i], y + dy[i]
#         if B[xx][yy] == 0 or ck[xx][yy] == 1:
#             continue
#         dfs(xx, yy)
#
#
# def process():
#     global B, ck
#     M, N, K = map(int, input().split())
#     B = [[0 for i in range(50 + 2)] for _ in range(50 + 2)]
#     ck = [[0 for i in range(50 + 2)] for _ in range(50 + 2)]
#     for _ in range(K):
#         X, Y = map(int, input().split())
#         B[Y + 1][X + 1] = 1
#     ans = 0
#     for i in range(1, N + 1):
#         for j in range(1, M + 1):
#             if B[i][j] == 0 or ck[i][j] == 1:
#                 continue
#             dfs(i, j)
#             ans += 1
#     print(ans)
#
#
# for _ in range(T):
#     B, ck = [], []
#     process()

import sys
from collections import deque
input = sys.stdin.readline

def bfs(row, col):
    q = deque([(row, col)])
    visited[row][col] = True
    while q:
        ro, co = q.popleft()
        for i in range(4):
            rr, cc = ro+dx[i], co+dy[i]
            if 0<=rr<n and 0<=cc<m:
                if not visited[rr][cc] and matrix[rr][cc]:
                    visited[rr][cc] = True
                    q.append((rr,cc))


t = int(input())
dx,dy = [-1,1,0,0],[0,0,-1,1]
for _ in range(t):
    m,n,k = map(int, input().split())
    matrix = [[0]*m for _ in range(n)]
    visited = [[False]*m for _ in range(n)]
    cnt = 0
    for _ in range(k):
        c,r = map(int, input().split())
        matrix[r][c] = 1
    for i in range(n):
        for j in range(m):
            if matrix[i][j] == 1 and not visited[i][j]:
                bfs(i,j)
                cnt += 1
    print(cnt)
