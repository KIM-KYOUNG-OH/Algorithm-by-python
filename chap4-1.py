n = int(input())
lst = list(input().split())
y, x = 1, 1
alp = ['R', 'L', 'D', 'U']
dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]
for i in lst:
    for j in range(len(alp)):
        if i == alp[j]:
            xx = x + dx[j]
            yy = y + dy[j]
        if xx < 1 or yy < 1 or xx > n or yy > n:
            continue
        x, y = xx, yy
print(y, x)
