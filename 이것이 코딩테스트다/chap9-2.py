# INF = int(1e9)
# n,m = map(int, input().split())
# graph = [[INF] * (n+1) for _ in range(n+1)]
# for i in range(1, n+1):
#     for j in range(1, n+1):
#         if i==j:
#             graph[i][j] = 0
# for _ in range(m):
#     r, c = map(int, input().split())
#     graph[r][c], graph[c][r] = 1, 1
# for k in range(1, n+1):
#     for i in range(1, n+1):
#         for j in range(1, n+1):
#             graph[i][j] = min(graph[i][j], graph[i][k] + graph[k][j])
# x, k = map(int, input().split())
# distance = graph[1][k] + graph[k][x]
# if distance < INF:
#     print(distance)
# else:
#     print(-1)
import heapq
import sys


def floyd_warshall(graph: list) -> list:
    n = len(graph) - 1
    INF = sys.maxsize
    distance = [[INF] * (n + 1) for _ in range(n + 1)]
    for i in range(1, n + 1):
        distance[i][i] = 0

    for a in range(1, n + 1):
        for b in graph[a]:
            distance[a][b] = 1

    for k in range(1, n + 1):
        for i in range(1, n + 1):
            for j in range(1, n + 1):
                distance[i][j] = min(distance[i][j], distance[i][k] + distance[k][j])

    return distance


n, m = map(int, sys.stdin.readline().rstrip().split())
graph = [[] for _ in range(n + 1)]
for _ in range(m):
    a, b = map(int, sys.stdin.readline().rstrip().split())
    graph[a].append(b)
    graph[b].append(a)
x, k = map(int, sys.stdin.readline().rstrip().split())

distance = floyd_warshall(graph)
answer = distance[1][k] + distance[k][x]
if answer >= sys.maxsize:
    print(-1)
    exit(1)
print(answer)


# 5 7
# 1 2
# 1 3
# 1 4
# 2 4
# 3 4
# 3 5
# 4 5
# 4 5

# 4 2
# 1 3
# 2 4
# 3 4