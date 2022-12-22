import heapq
import math


def solution(jobs):
    pq = []
    total, prev_start, current_time, cnt = 0, -1, 0, 0
    while cnt < len(jobs):
        for job in jobs:
            if prev_start < job[0] <= current_time:
                heapq.heappush(pq, [job[1], job[0]])
        if pq:
            elapsed_time, start_time = heapq.heappop(pq)
            prev_start = current_time
            current_time += elapsed_time
            total += current_time - start_time
            cnt += 1
        else:
            current_time += 1
    return math.floor(total / cnt)


print(solution([[0, 3], [1, 9], [2, 6]]))