import heapq
import sys
from collections import deque


def dijkstra(graph, n, start):
    INF = sys.maxsize
    distances = [INF] * (n + 1)
    distances[start] = 0
    pq = []
    heapq.heappush(pq, [0, start])
    while pq:
        cost, cur = heapq.heappop(pq)
        if distances[cur] < cost:
            continue

        for n_cost, next in graph[cur]:
            new_cost = cost + n_cost
            if distances[next] > new_cost:
                distances[next] = new_cost
                heapq.heappush(pq, [new_cost, next])
    return distances


n = int(sys.stdin.readline().rstrip())
m = int(sys.stdin.readline().rstrip())
graph = [[] for _ in range(n + 1)]
for _ in range(m):
    start, end, cost = map(int, sys.stdin.readline().rstrip().split())
    graph[start].append([cost, end])
start, end = map(int, sys.stdin.readline().rstrip().split())
distances = dijkstra(graph, n, start)
print(distances[end])