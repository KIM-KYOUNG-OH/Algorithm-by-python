import sys


def solution(alp, cop, problems):
    INF = sys.maxsize
    alp_max = 0
    cop_max = 0
    for problem in problems:
        alp_max = max(alp_max, problem[0])
        cop_max = max(cop_max, problem[1])
    dp = [[INF] * (cop_max + 1) for _ in range(alp_max + 1)]
    alp = min(alp, alp_max)
    cop = min(cop, cop_max)
    dp[alp][cop] = 0

    for i in range(alp, alp_max + 1):
        for j in range(cop, cop_max + 1):
            if i < alp_max:
                dp[i + 1][j] = min(dp[i + 1][j], dp[i][j] + 1)
            if j < cop_max:
                dp[i][j + 1] = min(dp[i][j + 1], dp[i][j] + 1)

            for alp_req, cop_req, alp_rwd, cop_rwd, cost in problems:
                if i < alp_req or j < cop_req:
                    continue
                new_alp = min(i + alp_rwd, alp_max)
                new_cop = min(j + cop_rwd, cop_max)
                dp[new_alp][new_cop] = min(dp[new_alp][new_cop], dp[i][j] + cost)
    return dp[alp_max][cop_max]


print(solution(10, 10, [[10,15,2,1,2],[20,20,3,3,4]]))