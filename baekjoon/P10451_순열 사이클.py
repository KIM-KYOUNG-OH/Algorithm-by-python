import sys
from collections import deque


def bfs(n, edges):
    cycle_cnt = 0
    cycle_components = []
    for i in range(1, n + 1):
        if i in cycle_components:
            continue
        q = deque([i])
        temp = [i]
        while q:
            node = q.popleft()
            if edges[node] == i:
                cycle_cnt += 1
                cycle_components += temp
                break
            temp.append(edges[node])
            q.append(edges[node])
    return cycle_cnt


t = int(sys.stdin.readline().rstrip())
answer = []
for _ in range(t):
    n = int(sys.stdin.readline().rstrip())
    lst = list(map(int, sys.stdin.readline().rstrip().split()))
    edges = dict()
    for i in range(len(lst)):
        edges[i + 1] = lst[i]
    answer.append(bfs(n, edges))
for i in answer:
    print(i)
