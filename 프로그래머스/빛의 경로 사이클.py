dy = [-1, 0, 1, 0]  # 북, 동, 남, 서
dx = [0, 1, 0, -1]


def get_path_length(i, j, k, grid):
    global visited
    cur_y, cur_x, cur_k = i, j, k
    cnt = 0
    visited[i][j][k] = True
    while True:
        cur_y = (cur_y + dy[cur_k]) % row
        cur_x = (cur_x + dx[cur_k]) % colum
        cnt += 1

        if grid[cur_y][cur_x] == 'R':
            cur_k = (cur_k + 1) % 4
        elif grid[cur_y][cur_x] == 'L':
            cur_k = (cur_k - 1) % 4
        if visited[cur_y][cur_x][cur_k]:
            if (cur_y, cur_x, cur_k) == (i, j, k):
                return cnt
            else:
                return 0
        visited[cur_y][cur_x][cur_k] = True


def solution(grid):
    global visited, row, colum
    row = len(grid)
    colum = len(grid[0])
    visited = [[[False for _ in range(4)] for _ in range(colum)] for _ in range(row)]
    answer = []
    for i in range(row):
        for j in range(colum):
            for k in range(4):
                if not visited[i][j][k]:
                    cnt = get_path_length(i, j, k, grid)
                    if cnt != 0:
                        answer.append(cnt)
    return sorted(answer)


print(solution(["R","R"]))