def solution(dirs):
    y = 5
    x = 5
    visited = [[[False, False, False, False] for _ in range(11)] for _ in range(11)]
    answer = 0
    direction = {'U': 0, 'R': 1, 'D': 2, 'L': 3}
    for dir in dirs:
        ny, nx = y, x
        if dir == 'U':
            ny = y - 1
        elif dir == 'D':
            ny = y + 1
        elif dir == 'R':
            nx = x + 1
        else:
            nx = x - 1
        if 0 <= ny <= 10 and 0 <= nx <= 10:
            if not visited[y][x][direction[dir]]:
                visited[y][x][direction[dir]] = True
                visited[ny][nx][(direction[dir] + 2) % 4] = True
                answer += 1
            y, x = ny, nx
    return answer


solution("LULLLLLLU")