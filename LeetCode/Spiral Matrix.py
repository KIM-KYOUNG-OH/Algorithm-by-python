dy = [0, 1, 0, -1]
dx = [1, 0, -1, 0]


class Solution:
    def spiralOrder(self, matrix):
        n = len(matrix)
        m = len(matrix[0])
        y, x = 0, 0
        visit = [[False] * m for _ in range(n)]
        direction = 0
        answer = []
        while True:
            visit[y][x] = True
            answer.append(matrix[y][x])
            ny = y + dy[direction]
            nx = x + dx[direction]
            if 0 <= ny < n and 0 <= nx < m:
                if not visit[ny][nx]:
                    y = ny
                    x = nx
                    continue
            direction = (direction + 1) % 4
            ny = y + dy[direction]
            nx = x + dx[direction]
            if 0 <= ny < n and 0 <= nx < m:
                if not visit[ny][nx]:
                    y = ny
                    x = nx
                    continue
            break
        return answer

