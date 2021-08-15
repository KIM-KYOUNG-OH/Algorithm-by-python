from collections import deque


def solution(n, computers):

    def dfs(com):
        nonlocal visited
        visited[com] = True
        for i in range(n):
            if com != i and computers[com][i] == 1:
                if not visited[i]:
                    visited[i] = True
                    dfs(i)

    # def bfs(com):
    #     nonlocal visited
    #     visited[com] = True
    #     q = deque([com])
    #     while q:
    #         com = q.popleft()
    #         visited[com] = True
    #         for i in range(n):
    #             if i != com and computers[com][i] == 1:
    #                 if not visited[i]:
    #                     q.append(i)

    answer = 0
    visited = [False for _ in range(n)]
    for com in range(n):
        if not visited[com]:
            dfs(com)
            answer += 1
    return answer


print(solution(3, [[1, 1, 0], [1, 1, 1], [0, 1, 1]]))