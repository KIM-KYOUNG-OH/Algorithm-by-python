import heapq
import sys


def dijkstra(graph, n):
    INF = sys.maxsize
    distance = [INF] * (n + 1)
    distance[1] = 0
    pq = []
    heapq.heappush(pq, (0, 1))
    while pq:
        cost, now = heapq.heappop(pq)
        if distance[now] < cost:
            continue
        for data in graph[now]:
            c, b = data
            new_cost = cost + c

            if new_cost < distance[b]:
                distance[b] = new_cost
                heapq.heappush(pq, (new_cost, b))
    return distance


def solution(n, roads, k):
    graph = [[] for _ in range(n + 1)]
    for road in roads:
        a, b, c = road
        graph[a].append([c, b])
        graph[b].append([c, a])

    distance = dijkstra(graph, n)
    answer = 0
    for i in range(1, n + 1):
        e = distance[i]
        if e <= k:
            answer += 1
    return answer


print(solution(6, [[1,2,1],[1,3,2],[2,3,2],[3,4,3],[3,5,2],[3,5,3],[5,6,1]], 4))