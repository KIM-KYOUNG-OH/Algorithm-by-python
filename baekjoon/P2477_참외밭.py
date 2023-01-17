import sys

k = int(sys.stdin.readline().rstrip())
cases = []
path = ''
max_width = 0
max_height = 0
for _ in range(6):
    direction, length = map(int, sys.stdin.readline().rstrip().split())
    cases.append([direction, length])
    if direction == 1 or direction == 2:
        max_width = max(max_width, length)
    else:
        max_height = max(max_height, length)
    path += str(direction)
cases.extend(cases)

dic = dict()
dic['423131' * 2] = [1, 3]
dic['314242' * 2] = [2, 4]
dic['314232' * 2] = [3, 2]
dic['314142' * 2] = [4, 1]
minus = 0
for key, value in dic.items():
    if path in key:
        for i in range(6):
            direction, length = cases[i]
            n_direction, n_length = cases[i + 1]
            if direction == value[0] and n_direction == value[1]:
                minus = length * n_length
                break
        break
print((max_width * max_height - minus) * k)