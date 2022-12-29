def solution(triangle):
    n = len(triangle)
    for i in range(n):
        for j in range(i + 1):
            if i == 0 and j == 0:
                continue
            elif j == 0:
                triangle[i][j] += triangle[i - 1][j]
            elif j == i:
                triangle[i][j] += triangle[i - 1][j - 1]
            else:
                triangle[i][j] = max(triangle[i][j] + triangle[i - 1][j - 1], triangle[i][j] + triangle[i - 1][j])
    return max(triangle[n - 1])


print(solution([[7], [3, 8], [8, 1, 0], [2, 7, 4, 4], [4, 5, 2, 6, 5]]))