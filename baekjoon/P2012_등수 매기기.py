import heapq
import sys

n = int(sys.stdin.readline().rstrip())
ranks = []
for _ in range(n):
    tmp = int(sys.stdin.readline().rstrip())
    heapq.heappush(ranks, tmp)

costs = [-1] * (n + 1)
rest = []
while ranks:
    cur = heapq.heappop(ranks)
    if costs[cur] == -1:
        costs[cur] = 0
    else:
        heapq.heappush(rest, cur)

idx = 1
answer = 0
while rest:
    cur = heapq.heappop(rest)
    while True:
        if idx > n:
            break
        elif costs[idx] == -1:
            answer += abs(cur - idx)
            break
print(answer)
