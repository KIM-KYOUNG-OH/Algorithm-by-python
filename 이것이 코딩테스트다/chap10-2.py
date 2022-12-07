# n,m = map(int, input().split())
# parent = [i for i in range(n+1)]
#
#
# def find_root(x):
#     if parent[x] != x:
#         parent[x] = find_root(parent[x])
#     return parent[x]
#
#
# def union(x, y):
#     x = find_root(x)
#     y = find_root(y)
#     if x < y:
#         parent[y] = x
#     else:
#         parent[x] = y
#
#
# for _ in range(m):
#     order, a, b = map(int, input().split())
#     if order == 1:
#         if find_root(a) == find_root(b):
#             print('YES')
#         else:
#             print('NO')
#     elif order == 0:
#         union(a, b)
import sys

n, m = map(int, sys.stdin.readline().rstrip().split())
parent = [i for i in range(n + 1)]


def union_parent(parent, a, b):
    a = find_parent(parent, a)
    b = find_parent(parent, b)
    if a < b:
        parent[b] = a
    else:
        parent[a] = b


def find_parent(parent, idx):
    if parent[idx] != idx:
        parent[idx] = find_parent(parent, parent[idx])
    return parent[idx]


for _ in range(m):
    order, a, b = map(int, sys.stdin.readline().rstrip().split())
    if order == 0:
        union_parent(parent, a, b)
    else:
        a_parent = find_parent(parent, a)
        b_parent = find_parent(parent, b)
        if a_parent == b_parent:
            print('YES')
        else:
            print('NO')

