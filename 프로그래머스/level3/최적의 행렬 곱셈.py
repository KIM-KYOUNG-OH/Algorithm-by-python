def solution(matrix_sizes):
    n = matrix_sizes
    dp = [[0] * n for _ in range(n)]

    for gap in range(1, n):
        for s in range(n - gap):
            e = s + gap
            candidates = list()
            for m in range(s, e):
                candidates.append(dp[s][m] + dp[m + 1][e] + matrix_sizes[s][0] * matrix_sizes[m][1] * matrix_sizes[e][1])
            dp[s][e] = min(candidates)
    return dp[0][-1]
