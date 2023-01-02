import heapq
import sys


def dijkstra(graph, n, start):
    INF = sys.maxsize
    distance = [INF] * (n + 1)
    pq = []
    distance[start] = 0
    heapq.heappush(pq, [0, start])
    while pq:
        cost, idx = heapq.heappop(pq)
        for i in graph[idx]:
            new_cost = cost + 1
            if distance[i] > new_cost:
                distance[i] = new_cost
                heapq.heappush(pq, [new_cost, i])
    return distance


def solution(n, edges):
    graph = [[] for _ in range(n + 1)]
    for a, b in edges:
        graph[a].append(b)
        graph[b].append(a)
    distance = dijkstra(graph, n, 1)
    distance = distance[1:]
    answer = 0
    for d in distance:
        if d == max(distance):
            answer += 1
    return answer


print(solution(6, [[3, 6], [4, 3], [3, 2], [1, 3], [1, 2], [2, 4], [5, 2]]))