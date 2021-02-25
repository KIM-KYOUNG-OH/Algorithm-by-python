n = input()
lst = list(n)
alp = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h']
x, y = 0, int(lst[1])
for i in range(len(alp)):
    if lst[0] == alp[i]:
        x = i + 1
cnt = 0
dx = [2, 2, -2, -2, 1, -1, 1, -1]
dy = [-1, 1, -1, 1, 2, 2, -2, -2]
for i in range(8):
    xx = x + dx[i]
    yy = y + dy[i]
    if xx < 1 or yy < 1 or xx > 8 or yy > 8:
        continue
    cnt += 1
print(cnt)
