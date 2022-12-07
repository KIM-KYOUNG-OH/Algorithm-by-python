# def find_parent(x):
#     if parent[x] != x:
#         parent[x] = find_parent(parent[x])
#     return parent[x]
#
#
# def union_parent(a, b):
#     a = find_parent(a)
#     b = find_parent(b)
#     if a < b:
#         parent[b] = a
#     else:
#         parent[a] = b
#
#
# n, m = map(int, input().split())
# parent = [i for i in range(n+1)]
# edges = []
# result = 0
# for _ in range(m):
#     a, b, cost = map(int, input().split())
#     edges.append((cost, a, b))
# edges.sort()
# last = 0
#
# for edge in edges:
#     cost, a, b = edge
#     if find_parent(a) != find_parent(b):
#         union_parent(a, b)
#         result += cost
#         last = cost
# print(result - last)
import sys

n, m = map(int, sys.stdin.readline().rstrip().split())
edges = []
for _ in range(m):
    a, b, c = map(int, sys.stdin.readline().rstrip().split())
    edges.append((c, a, b))
edges.sort()


def find_parent(parent, x):
    if parent[x] != x:
        parent[x] = find_parent(parent, parent[x])
    return parent[x]


def union_parent(parent, a, b):
    a = find_parent(parent, a)
    b = find_parent(parent, b)
    if a < b:
        parent[b] = a
    else:
        parent[a] = b


def kruskal(edges, n):
    parent = [i for i in range(n + 1)]
    max_cost = 0
    total = 0
    for edge in edges:
        c, a, b = edge
        a = find_parent(parent, a)
        b = find_parent(parent, b)
        if a != b:
            union_parent(parent, a, b)
            total += c
            if c > max_cost:
                max_cost = c
    return total - max_cost


cost = kruskal(edges, n)
print(cost)
