import heapq
import sys


def floyd_warshall(n, graph):
    INF = sys.maxsize
    distances = [[INF] * (n + 1) for _ in range(n + 1)]
    for i in range(n + 1):
        distances[i][i] = 0

    for A in range(1, n + 1):
        for B, cost in graph[A]:
            distances[A][B] = cost
            distances[B][A] = cost

    for k in range(1, n + 1):
        for i in range(1, n + 1):
            for j in range(1, n + 1):
                distances[i][j] = min(distances[i][j], distances[i][k] + distances[k][j])
    return distances


def solution(n, s, a, b, fares):
    graph = [[] for _ in range(n + 1)]
    for A, B, cost in fares:
        graph[A].append([B, cost])
        graph[B].append([A, cost])
    distances = floyd_warshall(n, graph)
    answer = sys.maxsize
    for i in range(1, n + 1):
        answer = min(answer, distances[s][i] + distances[i][a] + distances[i][b])
    return answer


print(solution(6, 4, 6, 2, [[4, 1, 10], [3, 5, 24], [5, 6, 2], [3, 1, 41], [5, 1, 24], [4, 6, 50], [2, 4, 66], [2, 3, 22], [1, 6, 25]]))