from collections import deque


def bfs(n, computers, visited, cur):
    visited[cur] = True
    q = deque()
    q.append(cur)
    while q:
        node = q.popleft()
        for i in range(n):
            if i == node:
                continue
            elif computers[node][i] == 1:
                if not visited[i]:
                    visited[i] = True
                    q.append(i)


def solution(n, computers):
    visited = [False] * n
    answer = 0
    for i in range(n):
        if not visited[i]:
            answer += 1
            bfs(n, computers, visited, i)
    return answer


print(solution(3, [[1, 1, 0], [1, 1, 0], [0, 0, 1]]))