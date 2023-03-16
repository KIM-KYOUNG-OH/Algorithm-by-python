class Solution:
    def rotate(self, matrix) -> None:
        n = len(matrix)
        for start in range(n // 2):
            end = n - start - 1
            l = end - start + 1
            for i in range(l - 1):
                temp = matrix[start][start + i]

                # 왼 -> 위
                matrix[start][start + i] = matrix[end - i][start]

                # 아래 -> 왼
                matrix[end - i][start] = matrix[end][end - i]

                # 오른 -> 아래
                matrix[end][end - i] = matrix[start + i][end]

                # 위 -> 오른
                matrix[start + i][end] = temp


Solution.rotate('', [[1,2,3],[4,5,6],[7,8,9]])
