def solution(board, skill):
    n, m = len(board), len(board[0])
    matrix = [[0] * (m + 1) for _ in range(n + 1)]
    for type, r1, c1, r2, c2, degree in skill:
        if type == 1:
            matrix[r1][c1] -= degree
            matrix[r2 + 1][c1] += degree
            matrix[r1][c2 + 1] += degree
            matrix[r2 + 1][c2 + 1] -= degree
        else:
            matrix[r1][c1] += degree
            matrix[r2 + 1][c1] -= degree
            matrix[r1][c2 + 1] -= degree
            matrix[r2 + 1][c2 + 1] += degree

    # 세로
    for i in range(n):
        for j in range(m):
            matrix[i + 1][j] += matrix[i][j]

    # 가로
    for i in range(n):
        for j in range(m):
            matrix[i][j + 1] += matrix[i][j]

    answer = 0
    for i in range(n):
        for j in range(m):
            score = board[i][j] + matrix[i][j]
            if score >= 1:
                answer += 1
    return answer


print(solution([[5,5,5,5,5],[5,5,5,5,5],[5,5,5,5,5],[5,5,5,5,5]], [[1,0,0,3,4,4],[1,2,0,2,3,2],[2,1,0,3,1,2],[1,0,1,3,3,1]]))