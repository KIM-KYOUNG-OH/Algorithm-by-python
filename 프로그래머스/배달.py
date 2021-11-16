import heapq


def dijkstra(min_distances, roads):
    heap = []
    heapq.heappush(heap, [0, 1])
    while heap:
        cost, node = heapq.heappop(heap)
        for c, n in roads[node]:
            if cost + c < min_distances[n]:
                min_distances[n] = cost + c
                heapq.heappush(heap, [cost + c, n])


def solution(N, road, K):
    answer = 0
    INF = int(1e9)
    min_distances = [INF] * (N + 1)
    min_distances[1] = 0
    roads = [[] for _ in range(N + 1)]
    for r in road:
        roads[r[0]].append([r[2], r[1]])
        roads[r[1]].append([r[2], r[0]])
    dijkstra(min_distances, roads)

    for idx, distance in enumerate(min_distances):
        if distance <= K:
            answer += 1

    return answer


print(solution(5, [[1,2,1],[2,3,3],[5,2,2],[1,4,2],[5,3,1],[5,4,2]], 3))