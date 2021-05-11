def draw_stars(depth, idx):
    if depth == 1:
        map[idx][idx] = '*'
        return
    l = 4 * (depth - 1) + 1
    for i in range(idx, idx + l):
        map[idx][i] = '*'
        map[idx + l - 1][i] = '*'
    for i in range(idx, idx + l):
        map[i][idx] = '*'
        map[i][idx + l - 1] = '*'
    draw_stars(depth - 1, idx + 2)


n = int(input())
length = 4 * (n - 1) + 1
map = [[' '] * length for _ in range(length)]
draw_stars(n, 0)
for i in range(length):
    for j in range(length):
        print(map[i][j], end='')
    print()