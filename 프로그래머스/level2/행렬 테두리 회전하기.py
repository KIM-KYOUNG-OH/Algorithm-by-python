def solution(rows, columns, queries):
    num = 1
    matrix = [[0 for _ in range(columns + 1)] for _ in range(rows + 1)]
    for i in range(1, rows + 1):
        for j in range(1, columns + 1):
            matrix[i][j] = num
            num += 1

    answer = []
    for query in queries:
        start_y = query[0]
        start_x = query[1]
        end_y = query[2]
        end_x = query[3]
        r = end_y - start_y + 1
        c = end_x - start_x + 1
        minimum = matrix[start_y][start_x]
        tmp = matrix[start_y][start_x]

        # 왼
        for i in range(r - 1):
            next = matrix[start_y + 1 + i][start_x]
            matrix[start_y + i][start_x] = next
            minimum = min(minimum, next)

        # 아래
        for i in range(c - 1):
            next = matrix[end_y][start_x + i + 1]
            matrix[end_y][start_x + i] = next
            minimum = min(minimum, next)

        # 오른
        for i in range(r - 1):
            next = matrix[end_y - i - 1][end_x]
            matrix[end_y - i][end_x] = next
            minimum = min(minimum, next)

        # 위
        for i in range(c - 1):
            if i == c - 2:
                matrix[start_y][end_x - i] = tmp
                break
            next = matrix[start_y][end_x - i - 1]
            matrix[start_y][end_x - i] = next
            minimum = min(minimum, next)

        answer.append(minimum)

    return answer


solution(6, 6, [[2,2,5,4],[3,3,6,6],[5,1,6,3]])