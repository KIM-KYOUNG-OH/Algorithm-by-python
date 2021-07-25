# import heapq
#
# def solution(scoville, K):
#     heap = []
#     count = 0
#     for i in scoville:
#         heapq.heappush(heap, i)
#     while heap[0] < K:
#         if len(heap)==1 and min(heap)<K:
#             return -1
#         heapq.heappush(heap, heapq.heappop(heap) + 2*heapq.heappop(heap))
#         count += 1
#     return count

import heapq


def solution(scoville, K):
    answer = 0  # 섞기 횟수
    heapq.heapify(scoville)
    while scoville[0] < K:  # heap의 최소값이 K보다 작을 때
        min_sv = heapq.heappop(scoville)  # 최소값
        if not scoville:  # 모든 음식의 스코빌 지수를 K 이상으로 만들수 없을 때
            return -1
        second_min_sv = heapq.heappop(scoville)  # 두 번째로 작은 값
        heapq.heappush(scoville, min_sv + second_min_sv * 2)  # 섞기
        answer += 1  # 섞기 횟수 + 1

    return answer


print(solution([1, 2, 3, 9, 10, 12],7))