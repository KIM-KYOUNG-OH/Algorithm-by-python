import sys


min_y = sys.maxsize
min_x = sys.maxsize
max_y = -sys.maxsize
max_x = -sys.maxsize


def findMeetPoint(left, right):
    a1 = left[0]
    b1 = left[1]
    c1 = left[2]
    a2 = right[0]
    b2 = right[1]
    c2 = right[2]
    y = -1.1
    if a1 * b2 - a2 * b1 != 0:
        y = (a2 * c1 - a1 * c2) / (a1 * b2 - a2 * b1)
    x = -1.1
    if a2 * b1 - a1 * b2 != 0:
        x = (b2 * c1 - b1 * c2) / (a2 * b1 - a1 * b2)
    return x, y


def solution(line):
    global min_y, min_x, max_y, max_x
    n = len(line)
    meet_points = list()
    for i in range(0, n):
        left = line[i]
        for j in range(i, n):
            right = line[j]
            x, y = findMeetPoint(left, right)
            if x == int(x) and y == int(y):
                y = int(y)
                x = int(x)
                min_y = min(min_y, y)
                min_x = min(min_x, x)
                max_y = max(max_y, y)
                max_x = max(max_x, x)
                # print("(y, x) = (", y, ", ", x, ")")
                if (y, x) not in meet_points:
                    meet_points.append((y, x))

    row = max_y - min_y + 1
    col = max_x - min_x + 1
    center_y = row // 2
    center_x = col // 2
    # print('center_y = ', center_y, ', center_x = ', center_x)
    matrix = [["."] * col for _ in range(row)]
    # print(matrix)
    for y, x in meet_points:
        # print('y = ', y, ', x = ', x)
        ny = max_y - y
        nx = x - min_x
        matrix[ny][nx] = '*'

    answer = []
    for i in range(0, len(matrix)):
        answer.append(''.join(matrix[i]))
    print(answer)
    return answer


solution([[2, -1, 4], [-2, -1, 4], [0, -1, 1], [5, -8, -12], [5, 8, 12]]	)