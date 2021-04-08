from collections import deque

n, m = map(int, input().split())
matrix = [list(map(int, list(input()))) for _ in range(n)]
visit = [[False] * m for _ in range(n)]
q = deque()

visit[0][0] = True
q.append((0, 0))
dx, dy = [-1,1,0,0], [0,0,-1,1]

while q:
    x, y = q.popleft()
    for j in range(4):
        xx, yy = x + dx[j], y + dy[j]
        if 0 <= xx < n and 0 <= yy < m:
            if matrix[xx][yy] == 1 and not visit[xx][yy]:
                print(xx, yy)
                matrix[xx][yy] = matrix[x][y] + 1
                q.append((xx, yy))
                visit[xx][yy] = True

# 제일 빠른 경로가 제일 먼저 matrix[n-1][m-1]값을 바꾸기 때문에
# 따로 최소값 처리를 안해줘도 된다
print(matrix[n-1][m-1])

# def dfs(r,c):
#     global ans
#     if r == n and c == m:
#         ans = min(ans, matrix[r][c])
#     for i in range(4):
#         rr = r + dx[i]
#         cc = c + dy[i]
#         if 0 < rr <= n and 0 < cc <= m:
#             if matrix[rr][cc] == 1 and not visited[rr][cc]:
#                 visited[rr][cc] = True
#                 matrix[rr][cc] += matrix[r][c]
#                 dfs(rr,cc)
#                 matrix[rr][cc] -= matrix[r][c]
#                 visited[rr][cc] = False
#
#
# n,m = map(int, input().split())
# ans = m*n
# matrix = [[0 for _ in range(m+1)] for _ in range(n+1)]
# visited = [[False for _ in range(m+1)] for _ in range(n+1)]
# visited[1][1] = True
# for i in range(n):
#     s = input()
#     for j in range(m):
#         matrix[i+1][j+1] = int(s[j])
# dx = [0,1,-1,0]
# dy = [1,0,0,-1]
# dfs(1,1)
# print(ans)