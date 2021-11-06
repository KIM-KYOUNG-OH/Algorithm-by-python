import heapq
import sys

n = int(sys.stdin.readline().rstrip())
heap = []
for _ in range(n):
    num = int(sys.stdin.readline().rstrip())
    if num != 0:
        heapq.heappush(heap, (abs(num), num))
    else:  # num == 0
        if len(heap) == 0:  # 힙이 비었을 때
            print(0)
        else:  # 힙에 데이터가 있을 때
            print(heapq.heappop(heap)[1])
