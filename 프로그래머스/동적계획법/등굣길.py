# def solution(m, n, puddles):
#     answer = [[0]*(m+1) for _ in range(n+1)]
#     answer[1][1] = 1
#     for i in range(1,n+1):
#         for j in range(1,m+1):
#             if i==1 and j==1:
#                 continue
#             if [j,i] in puddles:
#                 answer[i][j] = 0
#             else:
#                 answer[i][j] = answer[i-1][j] + answer[i][j-1]
#
#     return answer[n][m]%1000000007

def solution(m, n, puddles):
    graph = [[] for _ in range(n + 1)]
    for i in range(n + 1):
        for j in range(m + 1):
            if i == 0 or j == 0:
                graph[i].append(0)
            else:
                graph[i].append(1)

    for puddle in puddles:  # 웅덩이 0으로 표시
        col, row = puddle
        graph[row][col] = 0

    for i in range(1, n + 1):
        for j in range(1, m + 1):
            if i == 1 and j == 1:
                continue
            if graph[i][j] == 0:
                continue
            graph[i][j] = graph[i - 1][j] + graph[i][j - 1]

    return graph[-1][-1] % 1000000007


print(solution(4,3,[[2,2]]))