import sys

n, m, b = map(int, sys.stdin.readline().rstrip().split())
field = []
min_height = 256
max_height = 0
answer_time = int(1e9)
answer_height = 0

for _ in range(n):
    row = list(map(int, sys.stdin.readline().rstrip().split()))
    field.append(row)
    min_height = min(min_height, min(row))
    max_height = max(max_height, max(row))

for k in range(min_height, max_height+1):
    earn = 0
    use = 0
    for i in range(n):
        for j in range(m):
            if field[i][j] < k:
                use += k - field[i][j]
                continue
            if field[i][j] > k:
                earn += field[i][j] - k
                continue
    inventory = earn + b
    if inventory < use:
        continue
    time = 2 * earn + use
    if answer_time >= time:
        answer_time = time
        answer_height = k
print(answer_time, end=' ')
print(answer_height)



