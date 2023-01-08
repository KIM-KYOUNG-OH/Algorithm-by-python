import sys

n = int(sys.stdin.readline().rstrip())
rectangles = []
max_height = 0
for _ in range(n):
    tmp = list(map(int, sys.stdin.readline().rstrip().split()))
    max_height = max(max_height, tmp[1])
    rectangles.append(tmp)
rectangles = sorted(rectangles, key=lambda x: x[0])
# print('rectangles = ', rectangles)
# print('max_height = ', max_height)

prev_left_pos = rectangles[0][0]
prev_left_height = rectangles[0][1]
left_area = 0
for i in range(0, len(rectangles)):
    pos, height = rectangles[i]
    # print('pos = ', pos, ', height = ', height)
    if i != 0:
        left_area += (pos - prev_left_pos) * prev_left_height
        if prev_left_height <= height:
            prev_left_pos = pos
            prev_left_height = height
        else:
            prev_left_pos = pos
    # print('left_area = ', left_area)
    if height == max_height:
        break


prev_right_pos = rectangles[-1][0]
prev_right_height = rectangles[-1][1]
right_area = 0
for i in range(len(rectangles) - 1, -1, -1):
    pos, height = rectangles[i]
    # print('pos = ', pos, ', height = ', height)
    if i != len(rectangles) - 1:
        right_area += (prev_right_pos - pos) * prev_right_height
        if prev_right_height <= height:
            prev_right_pos = pos
            prev_right_height = height
        else:
            prev_right_pos = pos
    # print('right_area = ', right_area)
    if height == max_height:
        break
# print(prev_left_pos)
# print(prev_right_pos)
answer = left_area + right_area + (prev_right_pos - prev_left_pos + 1) * max_height
print(answer)




