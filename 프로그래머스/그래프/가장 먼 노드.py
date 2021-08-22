# from collections import deque
#
#
# def bfs(visited, graph):
#     q = deque([[1, 0]])
#     while q:
#         value = q.popleft()
#         v = value[0]
#         count = value[1]
#         if visited[v] == -1:
#             visited[v] = count
#             count += 1
#             for e in graph[v]:
#                 q.append([e, count])
#
#
# def solution(n, edge):
#     answer = 0
#     visited = [-1] * (n + 1)
#     graph = [[] for _ in range(n + 1)]
#     for e in edge:
#         x = e[0]
#         y = e[1]
#         graph[x].append(y)
#         graph[y].append(x)
#     bfs(visited, graph)
#     for value in visited:
#         if value == max(visited):
#             answer += 1
#     return answer
from collections import deque


def solution(n, edge):
    routes_dic = dict()
    for e1, e2 in edge:
        routes_dic.setdefault(e1, []).append(e2)
        routes_dic.setdefault(e2, []).append(e1)

    q = deque([[1, 0]])  # node index, depth
    check = [-1] * (n + 1)
    while q:
        index, depth = q.popleft()
        check[index] = depth
        for node in routes_dic[index]:
            if check[node] == -1:
                check[node] = 0
                q.append([node, depth + 1])
    return check.count(max(check))


print(solution(6,[[3, 6], [4, 3], [3, 2], [1, 3], [1, 2], [2, 4], [5, 2]]))