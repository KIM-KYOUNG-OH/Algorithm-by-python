def solution(grid):
    dy = [-1, 0, 1, 0]
    dx = [0, 1, 0, -1]
    row = len(grid)
    col = len(grid[0])
    answer = []
    visited = [[[False] * 4 for _ in range(col)] for _ in range(row)]
    for i in range(row):
        for j in range(col):
            for dir in range(4):
                ny, nx = i, j
                cnt = 0
                if visited[ny][nx][dir]:
                    continue
                while not visited[ny][nx][dir]:
                    visited[ny][nx][dir] = True
                    cnt += 1
                    order = grid[ny][nx]
                    if order == 'S':
                        pass
                    elif order == 'R':
                        dir = (dir + 1) % 4
                    elif order == 'L':
                        dir = (dir - 1) % 4
                    ny = (ny + dy[dir]) % row
                    nx = (nx + dx[dir]) % col
                answer.append(cnt)
    answer.sort()
    print(answer)
    return answer

solution(["R","R"])