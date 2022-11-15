from collections import deque
import copy, sys


def getCountOfTowers(n, graph, node):
    global unused_node
    q = deque([])
    q.append(node)
    visited = [False for _ in range(n + 1)]
    visited[node] = True
    count = 1
    while q:
        cur = q.pop()
        for i in graph[cur]:
            if not visited[i]:
                visited[i] = True
                q.append(i)
                count += 1
                unused_node.remove(i)
    return count

def solution(n, wires):
    global unused_node
    graph = [[] for _ in range(0, n + 1)]
    for wire in wires:
        a, b = wire
        graph[a].append(b)
        graph[b].append(a)

    answer = sys.maxsize
    for wire in wires:
        a, b = wire
        unused_node = [i for i in range(1, n + 1)]
        graph_copied = copy.deepcopy(graph)
        graph_copied[a].remove(b)
        graph_copied[b].remove(a)
        left = getCountOfTowers(n, graph_copied, unused_node.pop())
        right = getCountOfTowers(n, graph_copied, unused_node.pop())
        diff = abs(left - right)
        if diff < answer:
            answer = diff
    if answer == sys.maxsize:
        answer = 0

    return answer


unused_node = []
solution(7, [[1,2],[2,7],[3,7],[3,4],[4,5],[6,7]])