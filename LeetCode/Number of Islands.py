from collections import deque

dy = [-1, 0, 1, 0]
dx = [0, 1, 0, -1]


class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        n, m = len(grid), len(grid[0])
        visit = [[False] * m for _ in range(n)]
        answer = 0
        for i in range(n):
            for j in range(m):
                if visit[i][j] or grid[i][j] == '0':
                    continue

                q = deque()
                q.append((i, j))
                visit[i][j] = True
                answer += 1
                while q:
                    y, x = q.popleft()
                    for k in range(4):
                        ny = y + dy[k]
                        nx = x + dx[k]
                        if 0 <= ny < n and 0 <= nx < m:
                            if not visit[ny][nx] and grid[ny][nx] == '1':
                                visit[ny][nx] = True
                                q.append((ny, nx))
        return answer