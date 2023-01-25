import heapq
import sys

n = int(sys.stdin.readline().rstrip())
visit = [False] * 500001
pq = []
for _ in range(n):
    num = int(sys.stdin.readline().rstrip())
    if not visit[num] and num <= n:
        visit[num] = True
    else:
        heapq.heappush(pq, num)

answer = 0
for i in range(1, n + 1):
    if visit[i]:
        continue

    cur = heapq.heappop(pq)
    answer += abs(i - cur)
print(answer)