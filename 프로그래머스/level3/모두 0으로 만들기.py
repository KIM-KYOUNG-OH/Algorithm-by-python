from collections import deque
from collections import defaultdict


def find_tree(a, edges):
    graph = defaultdict(list)
    for v1, v2 in edges:
        graph[v1].append(v2)
        graph[v2].append(v1)

    q = deque([(-1, 0)])
    path = []
    visited = [False] * len(a)
    visited[0] = True

    while q:
        p, c = q.popleft()
        path.append((p, c))
        for node in graph[c]:
            if not visited[node]:
                q.append((c, node))
                visited[node] = True
    return path[::-1]


def solution(a, edges):
    answer = 0
    path = find_tree(a, edges)  # bfs reverse 경로

    for parent, child in path[:-1]:
        c_weight = a[child]
        answer += abs(c_weight)
        a[child] = 0
        a[parent] += c_weight

    if a[0] == 0:
        return answer
    else:
        return -1


print(solution([-5,0,2,1,2], [[0,1],[3,4],[2,3],[0,3]]))
# print(solution([0,1,0], [[0,1],[1,2]]))
# print(solution([0,1], [[0,1]]))