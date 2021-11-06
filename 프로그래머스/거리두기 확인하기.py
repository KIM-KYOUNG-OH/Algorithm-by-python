from collections import deque


def bfs(place, i, j):
    dy = [-1, 0, 1, 0]
    dx = [0, -1, 0, 1]
    visited = [[False for _ in range(5)] for _ in range(5)]
    q = deque()
    q.append([i, j, 0])
    visited[i][j] = True
    while q:
        y, x, step = q.popleft()
        if 0 < step <= 2 and place[y][x] == 'P':
            return False
        if step >= 3:
            break
        for k in range(4):
            ny = y + dy[k]
            nx = x + dx[k]
            if 0 <= ny < 5 and 0 <= nx < 5:
                if place[ny][nx] != 'X' and not visited[ny][nx]:
                    visited[ny][nx] = True
                    q.append([ny, nx, step + 1])
    return True


def solution(places):
    answer = []
    for place in places:
        status = True
        for i in range(5):
            for j in range(5):
                if place[i][j] == 'P':
                    if not bfs(place, i, j):
                        status = False
                        break
            if not status:
                break
        if not status:
            answer.append(0)
        else:
            answer.append(1)
    return answer