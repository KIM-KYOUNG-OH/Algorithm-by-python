import heapq


def solution(scoville, K):
    answer = 0
    pq = []
    for e in scoville:
        heapq.heappush(pq, e)
    while scoville:
        if pq[0] >= K:
            break
        if len(pq) == 1:
            return -1
        a = heapq.heappop(pq)
        b = heapq.heappop(pq)
        heapq.heappush(pq, a + b * 2)
        answer += 1
    return answer


print(solution([1, 2, 3, 9, 10, 12], 7))
