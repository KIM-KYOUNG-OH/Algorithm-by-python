import heapq

def solution(scoville, K):
    heap = []
    count = 0
    for i in scoville:
        heapq.heappush(heap, i)
    while heap[0] < K:
        if len(heap)==1 and min(heap)<K:
            return -1
        heapq.heappush(heap, heapq.heappop(heap) + 2*heapq.heappop(heap))
        count += 1
    return count

print(solution([1, 2, 3, 9, 10, 12],7))