# def solution(triangle):
#     cases = []
#     cases.append(triangle[0])
#     if len(triangle)==1:
#         return triangle[0][0]
#     for i in range(len(triangle)-1):
#         temp = []
#         for j in range(len(triangle[i])):
#             temp.append(cases[i][j] + triangle[i + 1][j])
#             if j!=0:
#                 if temp[-2]>=temp[-1]:
#                     temp.pop()
#                 elif temp[-2]<temp[-1]:
#                     temp.pop(-2)
#             temp.append(cases[i][j] + triangle[i + 1][j+1])
#         cases.append(temp)
#
#     return max(cases[-1])

def solution(triangle):
    dp = [[0] * (i + 1) for i in range(len(triangle))]
    dp[0][0] = triangle[0][0]
    for i in range(1, len(triangle)):
        for j in range(i + 1):
            if j == 0:  # 행의 첫번째 요소
                dp[i][j] = dp[i - 1][j] + triangle[i][j]
            elif j == i:  # 행의 마지막 요소
                dp[i][j] = dp[i - 1][j - 1] + triangle[i][j]
            else:  # 그외 요소
                dp[i][j] = max(dp[i - 1][j - 1], dp[i - 1][j]) + triangle[i][j]
    return max(dp[-1])


print(solution([[7], [3, 8], [8, 1, 0], [2, 7, 4, 4], [4, 5, 2, 6, 5]]))