answer = False
dy = [-1, 0, 1, 0]
dx = [0, 1, 0, -1]


def dfs(n, m, board, word, visit, y, x, path):
    global answer
    if answer:
        return
    if path == word:
        answer = True
        return

    for k in range(4):
        ny = y + dy[k]
        nx = x + dx[k]
        if 0 <= ny < n and 0 <= nx < m:
            if not visit[ny][nx] and board[ny][nx] == word[len(path)]:
                visit[ny][nx] = True
                dfs(n, m, board, word, visit, ny, nx, path + board[ny][nx])
                visit[ny][nx] = False


class Solution:
    def exist(self, board, word: str) -> bool:
        global answer
        answer = False
        n = len(board)
        m = len(board[0])
        visit = [[False] * m for _ in range(n)]
        for i in range(n):
            for j in range(m):
                if board[i][j] == word[0] and not answer:
                    visit[i][j] = True
                    dfs(n, m, board, word, visit, i, j, board[i][j])
                    visit[i][j] = False
        return answer


print(Solution.exist('', [["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]], 'ABCCED'))
# print(Solution.exist('', [["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]], 'ABCCED'))
# print(Solution.exist('', [["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]], 'ABCB'))
