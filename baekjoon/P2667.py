from collections import deque


def bfs(i, j):
    cnt = 1
    q = deque([(i,j)])
    visited[i][j] = True
    while q:
        r,c = q.popleft()
        for k in range(4):
            rr, cc = r+dx[k], c+dy[k]
            if 0<=rr<n and 0<=cc<n:
                if not visited[rr][cc] and matrix[rr][cc] == 1:
                    visited[rr][cc] = True
                    q.append((rr,cc))
                    cnt += 1
    return cnt


n = int(input())
matrix = [list(map(int, list(input()))) for _ in range(n)]
visited = [[False]*n for _ in range(n)]
ans = []
dx, dy = [-1,0,1,0], [0,-1,0,1]
for i in range(n):
    for j in range(n):
        if not visited[i][j] and matrix[i][j] == 1:
            ans.append(bfs(i,j))
print(len(ans))
ans.sort()
for data in ans:
    print(data)