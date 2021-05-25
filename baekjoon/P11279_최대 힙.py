import heapq
import sys

n = int(sys.stdin.readline().rstrip())
lst = []
for _ in range(n):
    num = int(sys.stdin.readline().rstrip())
    if num == 0:
        if len(lst) == 0:
            print(0)
            continue
        print(-heapq.heappop(lst))
        continue
    heapq.heappush(lst, -num)

