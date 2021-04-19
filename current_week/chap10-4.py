import copy
from collections import deque

v = int(input())
graph = [[] for _ in range(v+1)]
indegree = [0] * (v+1)
times = [0] * (v+1)
for i in range(1, v+1):
    data = list(map(int, input().split()))
    times[i] = data[0]
    for j in data[1:-1]:
        indegree[i] += 1
        graph[j].append(i)


def topology_sort():
    result = copy.deepcopy(times)
    q = deque()
    for i in range(1, v+1):
        if indegree[i] == 0:
            q.append(i)
    while q:
        now = q.popleft()
        for i in graph[now]:
            result[i] = max(result[i], result[now] + times[i])
            indegree[i] -= 1
            if indegree[i] == 0:
                q.append(i)
    return result


ans = topology_sort()
for i in range(1, v+1):
    print(ans[i])