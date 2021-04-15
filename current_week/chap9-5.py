import heapq
import sys
input = sys.stdin.readline
INF = int(1e9)


def dijkstra(start):
    q = []
    heapq.heappush(q, (start, 0))
    distance_table[start] = 0
    while q:
        now, dist = heapq.heappop(q)
        if dist > distance_table[now]:
            continue
        for i in graph[now]:
            cost = i[1] + dist
            if cost < distance_table[i[0]]:
                distance_table[i[0]] = cost
                heapq.heappush(q, (i[0], cost))
                # (비용, 노드)로 바꾸자 heap에 정렬되야함


n, m, c = map(int, input().split())
distance_table = [INF] * (n+1)
graph = [[] for _ in range(n+1)]
for _ in range(m):
    node_a, node_b, cost = map(int,input().split())
    graph[node_a].append((node_b, cost))

dijkstra(c)

cnt = 0
max_distance = 0
for i in range(1, n+1):
    if distance_table[i] != INF:
        cnt += 1
        max_distance = max(max_distance, distance_table[i])
print(cnt-1, max_distance)