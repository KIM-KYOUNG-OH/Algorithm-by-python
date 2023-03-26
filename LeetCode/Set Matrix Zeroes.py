class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        zeroes = []
        m = len(matrix)
        n = len(matrix[0])
        for i in range(m):
            for j in range(n):
                if matrix[i][j] == 0:
                    zeroes.append((i, j))

        while zeroes:
            y, x = zeroes.pop()

            # row
            for i in range(m):
                matrix[i][x] = 0

            # col
            for i in range(n):
                matrix[y][i] = 0

        return matrix