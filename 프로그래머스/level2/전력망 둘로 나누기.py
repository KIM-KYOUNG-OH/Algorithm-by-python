from collections import deque


def solution(n, wires):
    graph = [[] for _ in range(n + 1)]
    for a, b in wires:
        graph[a].append(b)
        graph[b].append(a)
    answer = 100
    for i in range(n - 1):
        a = wires[i][0]
        b = wires[i][1]
        graph[a].remove(b)
        graph[b].remove(a)
        cnt1 = 1
        cnt2 = 1
        visited = [False] * (n + 1)
        q1 = deque([a])
        q2 = deque([b])
        visited[a] = True
        visited[b] = True
        while q1:
            cur = q1.popleft()
            for e in graph[cur]:
                if not visited[e]:
                    visited[e] = True
                    q1.append(e)
                    cnt1 += 1

        while q2:
            cur = q2.popleft()
            for e in graph[cur]:
                if not visited[e]:
                    visited[e] = True
                    q2.append(e)
                    cnt2 += 1
        diff = abs(cnt1 - cnt2)
        answer = min(diff, answer)
        graph[a].append(b)
        graph[b].append(a)
    return answer


print(solution(9, [[1,3],[2,3],[3,4],[4,5],[4,6],[4,7],[7,8],[7,9]]))
