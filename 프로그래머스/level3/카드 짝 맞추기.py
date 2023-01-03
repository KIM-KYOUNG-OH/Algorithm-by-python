import sys
from collections import deque, defaultdict
from copy import deepcopy
from itertools import permutations

dy = [-1, 0, 1, 0]
dx = [0, 1, 0, -1]


def dfs(board, numbers, candidate, r, c, idx, cost):
    if idx == len(candidate):
        return cost
    pos_arr = numbers[candidate[idx]]
    r1 = pos_arr[0][0]
    c1 = pos_arr[0][1]
    r2 = pos_arr[1][0]
    c2 = pos_arr[1][1]
    cost1 = getCost(board, r, c, r1, c1)
    cost2 = getCost(board, r, c, r2, c2)
    cost3 = getCost(board, r1, c1, r2, c2)
    cost4 = getCost(board, r2, c2, r1, c1)  # cost3 != cost4인 경우가 있다???
    new_board = deepcopy(board)
    new_board[r1][c1] = 0
    new_board[r2][c2] = 0

    # 분기????
    if cost1 < cost2:
        return dfs(new_board, numbers, candidate, r2, c2, idx + 1, cost + cost1 + 1 + cost3 + 1)
    else:
        return dfs(new_board, numbers, candidate, r1, c1, idx + 1, cost + cost2 + 1 + cost4 + 1)


def getCost(board, y1, x1, y2, x2):
    if y1 == y2 and x1 == x2:
        return 0
    q = deque()
    q.append([0, y1, x1])
    visited = [[False] * 4 for _ in range(4)]
    visited[y1][x1] = True
    while q:
        cost, y, x = q.popleft()
        if y == y2 and x == x2:
            return cost
        for k in range(4):
            ny = y + dy[k]
            nx = x + dx[k]
            if 0 <= ny < 4 and 0 <= nx < 4:
                if not visited[ny][nx]:
                    visited[ny][nx] = True
                    q.append([cost + 1, ny, nx])

            nny, nnx = ctrlMove(board, y, x, k)
            if not visited[nny][nnx]:
                visited[nny][nnx] = True
                q.append([cost + 1, nny, nnx])


def ctrlMove(board, y, x, k):
    while True:
        ny = y + dy[k]
        nx = x + dx[k]
        if 0 <= ny < 4 and 0 <= nx < 4:
            y = ny
            x = nx
            if board[y][x] != 0:
                break
        else:
            break
    return y, x


def solution(board, r, c):
    answer = float('inf')
    numbers = defaultdict(list)
    for i in range(4):
        for j in range(4):
            if board[i][j] != 0:
                numbers[board[i][j]].append([i, j])
    candidates = permutations(numbers.keys())
    for candidate in candidates:
        answer = min(answer, dfs(board, numbers, candidate, r, c, 0, 0))
    return answer


print(solution([[1,0,0,3],[2,0,0,0],[0,0,0,2],[3,0,1,0]], 1, 0))
# print(solution([[0, 0, 0, 1], [0, 0, 0, 0], [0, 1, 0, 0], [0, 0, 0, 0]], 0, 3)
# print(solution([[0, 0, 0, 1], [0, 0, 0, 0], [0, 1, 0, 0], [0, 0, 0, 0]], 0, 3))
