def find_parent(parent, a):
    if parent[a] != a:
        parent[a] = find_parent(parent, parent[a])
    return parent[a]


def union_parent(parent, a, b):
    pa = find_parent(parent, a)
    pb = find_parent(parent, b)
    if pa <= pb:
        parent[pb] = pa
    else:
        parent[pa] = pb


def kruskal(edges, n):
    edges.sort()
    parent = [i for i in range(n + 1)]
    answer = 0
    for cost, a, b in edges:
        if find_parent(parent, a) != find_parent(parent, b):
            union_parent(parent, a, b)
            answer += cost
    return answer


def solution(n, costs):
    edges = []
    for cost in costs:
        a, b, cost = cost
        edges.append([cost, a, b])
    answer = kruskal(edges, n)
    return answer
