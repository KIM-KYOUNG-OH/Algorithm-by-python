n,m = map(int, input().split())
parent = [i for i in range(n+1)]


def find_root(x):
    if parent[x] != x:
        parent[x] = find_root(parent[x])
    return parent[x]


def union(x, y):
    x = find_root(x)
    y = find_root(y)
    if x < y:
        parent[y] = x
    else:
        parent[x] = y


for _ in range(m):
    order, a, b = map(int, input().split())
    if order == 1:
        if find_root(a) == find_root(b):
            print('YES')
        else:
            print('NO')
    elif order == 0:
        union(a, b)