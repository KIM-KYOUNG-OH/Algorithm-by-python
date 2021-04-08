# from sys import stdin
# from collections import deque
#
#
# def bfs(matrix, q):
#     cnt = -1
#     dx, dy = [1, -1, 0, 0], [0, 0, -1, 1]
#     while q:
#         for _ in range(len(q)):
#             r, c = q.popleft()
#             for k in range(4):
#                 rr, cc = r + dx[k], c + dy[k]
#                 if 0 <= rr < n and 0 <= cc < m:
#                     if matrix[rr][cc] == 0:
#                         matrix[rr][cc] = 1
#                         q.append((rr, cc))
#         cnt += 1
#     for row in matrix:
#         if 0 in row:
#             return -1
#     return cnt
#
#
# m, n = map(int, stdin.readline().split())
# box = []
# queue = deque()
# for i in range(n):
#     row = list(map(int, list(stdin.readline().split())))
#     for j in range(m):
#         if row[j] == 1:
#             queue.append((i, j))
#     box.append(row)
#
# print(bfs(box, queue))

from collections import deque

def sol():
    ans = 0
    for i in range(r):
        for j in range(c):
            if matrix[i][j] == 0:
                return -1
            ans = max(ans, matrix[i][j])
    return ans-1

c,r = map(int, input().split())
matrix = []
q = deque()
dx, dy = [-1,0,1,0], [0,-1,0,1]
for i in range(r):
    row = list(map(int, input().split()))
    for j in range(c):
        if row[j] == 1:
            q.append((i,j))
    matrix.append(row)
while q:
    ro, co = q.popleft()
    for i in range(4):
        rr = ro + dx[i]
        cc = co + dy[i]
        if -1<rr<r and -1<cc<c:
            if matrix[rr][cc] == 0:
                q.append((rr, cc))
                matrix[rr][cc] = matrix[ro][co]+1
print(sol())