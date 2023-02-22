import heapq
import sys


def dijkstra(n, graph, start):
    INF = sys.maxsize
    distances = [INF] * (n + 1)
    distances[start] = 0
    pq = []
    heapq.heappush(pq, (0, start))
    while pq:
        cost, cur = heapq.heappop(pq)
        if distances[cur] < cost:
            continue

        for next in graph[cur]:
            new_cost = cost + 1
            if new_cost <= distances[next]:
                distances[next] = new_cost
                heapq.heappush(pq, (new_cost, next))
    return distances


def solution(n, roads, sources, destination):
    graph = [[] for _ in range(n + 1)]
    for a, b in roads:
        graph[a].append(b)
        graph[b].append(a)

    distances = dijkstra(n, graph, destination)
    result = []
    for source in sources:
        tmp = distances[source]
        if tmp == sys.maxsize:
            result.append(-1)
        else:
            result.append(tmp)
    return result


print(solution(3, [[1, 2], [2, 3]], [2, 3], 1))