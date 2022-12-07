# import copy
# from collections import deque
#
# v = int(input())
# graph = [[] for _ in range(v+1)]
# indegree = [0] * (v+1)
# times = [0] * (v+1)
# for i in range(1, v+1):
#     data = list(map(int, input().split()))
#     times[i] = data[0]
#     for j in data[1:-1]:
#         indegree[i] += 1
#         graph[j].append(i)
#
#
# def topology_sort():
#     result = copy.deepcopy(times)
#     q = deque()
#     for i in range(1, v+1):
#         if indegree[i] == 0:
#             q.append(i)
#     while q:
#         now = q.popleft()
#         for i in graph[now]:
#             result[i] = max(result[i], result[now] + times[i])
#             indegree[i] -= 1
#             if indegree[i] == 0:
#                 q.append(i)
#     return result
#
#
# ans = topology_sort()
# for i in range(1, v+1):
#     print(ans[i])
import sys
from collections import deque

n = int(sys.stdin.readline().rstrip())
indegree = [0] * (n + 1)
graph = [[] for _ in range(n + 1)]
for i in range(1, n + 1):
    arr = map(int, sys.stdin.readline().rstrip().split())
    time = arr[0]
    needs = arr[1:-1]
    for need in needs:
        graph[i].append((time, need))
        indegree[i] += 1


def topology_sort(graph, indegree, n):
    q = deque()
    for i in range(1, n + 1):
        if indegree[i] == 0:
            q.append(i)


answer = topology_sort(graph, indegree, n)
print(answer)