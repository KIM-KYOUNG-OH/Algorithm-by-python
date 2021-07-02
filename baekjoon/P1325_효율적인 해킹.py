import sys
from collections import deque


def bfs(start):
    q = deque([start])
    visited = [False] * (n + 1)  # 방문 여부 기록
    visited[start] = True  # 해킹 시작 노드는 방문 체크
    hacking_cnt = 1  # 해킹 횟수
    while q:
        com = q.popleft()
        for i in graph[com]:
            if not visited[i]:
                q.append(i)
                visited[i] = True
                hacking_cnt += 1
    return hacking_cnt


n, m = map(int, sys.stdin.readline().rstrip().split())
graph = [[] for _ in range(n + 1)]
for _ in range(m):
    A, B = map(int, sys.stdin.readline().rstrip().split())
    graph[B].append(A)

answer = []  # 한번에 가장 많은 해킹을 할 수 있는 컴퓨터 번호들을 저장
max_cnt = 1  # 가장 많이 해킹할 때 해킹 수
for i in range(1, n + 1):
    cnt = bfs(i)
    if max_cnt < cnt:
        answer = [i]  # 초기화
        max_cnt = cnt  # 해킹 수 초기화
    elif max_cnt == cnt:
        answer.append(i)
answer.sort()
print(' '.join(map(str, answer)))
