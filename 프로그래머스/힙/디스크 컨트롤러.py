# import heapq
#
#
# def solution(jobs):
#     answer, now = 0, 0  # 총 작업 시간, 현재 시간
#     heap = []
#     for job in jobs:
#         start_time, elapsed_time = job[0], job[1]  # 작업 요청 시간, 소요 시간
#         heapq.heappush(heap, (elapsed_time, start_time))
#     while heap:
#         elapsed_time, start_time = heap[0]
#         if start_time <= now:
#             now += elapsed_time  # 현재 시간 업데이트
#             heapq.heappop(heap)
#             answer += (now - start_time)  # 요청부터 종료까지 시간 더하기
#         else:  # 하드디스크가 작업을 수행하고 있지 않을 때에는 먼저 요청이 들어온 작업부터 처리
#             heap.sort(key=lambda x: -x[1])  # 요청시간기준 내림차순 정렬
#             elapsed_time, start_time = heap.pop()
#             now += elapsed_time  # 현재 시간 업데이트
#             answer += (now - start_time)  # 요청부터 종료까지 시간 더하기
#             heapq.heapify(heap)
#
#     return int(answer / len(jobs))

import heapq


def solution(jobs):  # jobs는 요청 시점순으로 정렬되있음
    answer, start, now, i = 0, -1, 0, 0
    heap = []

    while i < len(jobs):
        for job in jobs:
            start_time, elapsed_time = job[0], job[1]
            if start < start_time <= now:
                heapq.heappush(heap, [elapsed_time, start_time])
        if len(heap) > 0:
            elapsed_time, start_time = heapq.heappop(heap)
            start = now
            now += elapsed_time
            answer += (now - start_time)
            i += 1
        else:
            now += 1
    return int(answer / len(jobs))


print(solution([[0, 9], [1, 6], [2, 3]]))
