# from sys import stdin
# from collections import deque
#
#
# def bfs(result, visit, n, k):
#     q = deque()
#     q.append(n)
#     visit[n] = True
#     while q:
#         i = q.popleft()
#         if i == k:
#             return result[i]
#         for j in (i+1, i-1, i*2):
#             if 0 <= j < 100001 and visit[j] == False:
#                 visit[j] = True
#                 q.append(j)
#                 result[j] = result[i] + 1
#
#
# n, k = map(int, stdin.readline().split())
# visit = [False] * 100001
# result = [0] * 100001
# print(bfs(result, visit, n, k))

from collections import deque


def bfs(n):
    q = deque([n])
    visited[n] = True
    while q:
        pos = q.popleft()
        if pos == k:
            return result[pos]
        for move in (pos-1, pos+1, pos*2):
            if 0<=move<100001 and not visited[move]:
                q.append(move)
                visited[move] = True
                result[move] = result[pos] + 1


n,k = map(int,input().split())
visited = [False]*100001
result = [0]*100001
print(bfs(n))