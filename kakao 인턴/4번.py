from collections import deque


def solution(n, start, end, roads, traps):
    answer = 0
    graph = [[0] * (n+1) for _ in range(n+1)]
    for road in roads:
        p, q, s = road
        if graph[p][q]:  # 이미 경로가 있다면
            graph[p][q] = min(graph[p][q], s)
            continue
        graph[p][q] = s
    q = deque([(0, start)])  # (total, current_node)
    while q:
        total, current_node = q.popleft()
        if current_node == end:
            answer = total
            break
        for i in range(1, n+1):
            cost = graph[current_node][i]
            if cost > 0:
                q.append((total + cost, i))
                if i in traps:
                    for u in range(1, n+1):
                        for v in range(u+1, n+1):
                            if graph[u][v] != graph[v][u]:
                                graph[u][v], graph[v][u] = graph[v][u], graph[u][v]
                    break

    return answer