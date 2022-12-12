import heapq
from collections import defaultdict


def dijkstra(n, graph, gates, summits):
    summits_set = set(summits)
    INF = int(1e7) + 1
    pq = []
    intensities = [INF] * (n + 1)
    for gate in gates:
        heapq.heappush(pq, (0, gate))
        intensities[gate] = 0

    while pq:
        intensity, cur = heapq.heappop(pq)

        if cur in summits_set or intensity > intensities[cur]:
            continue

        for cost, b in graph[cur]:
            new_intensity = max(intensity, cost)
            if new_intensity < intensities[b]:
                intensities[b] = new_intensity
                heapq.heappush(pq, (new_intensity, b))

    return intensities


def solution(n, paths, gates, summits):
    graph = defaultdict(list)
    for a, b, c in paths:
        graph[a].append((c, b))
        graph[b].append((c, a))

    summits = sorted(summits)
    intensities = dijkstra(n, graph, gates, summits)
    answer = [0, int(1e7) + 1]
    for summit in summits:
        if intensities[summit] < answer[1]:
            answer = [summit, intensities[summit]]
    return answer


print(solution(7, [[1, 2, 5], [1, 4, 1], [2, 3, 1], [2, 6, 7], [4, 5, 1], [5, 6, 1], [6, 7, 1]], [3, 7], [1, 5]))