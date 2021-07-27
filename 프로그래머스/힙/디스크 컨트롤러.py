# import heapq
#
# def solution(jobs):
#     answer,now,i = 0,0,0
#     start = -1
#     heap = []
#
#     while i < len(jobs):
#         for j in jobs:
#             if start < j[0] <= now:
#                 heapq.heappush(heap, [j[1], j[0]])
#                 # [소요시간, 시작시간]
#         if len(heap) > 0:
#             current = heapq.heappop(heap)
#             start = now
#             now += current[0]
#             answer += (now-current[1])
#             i += 1
#         else:
#             now += 1
#     return int(answer/len(jobs))
def solution(jobs):
    answer = 0
    jobs_sorted = sorted(jobs, key=lambda x: x[1])  # stack, 작업 소요 시간 기준 내림차순 정렬
    time = 0  # 현재 시간
    while jobs_sorted:
        job = jobs_sorted.pop()
        if time <= job[0]:
            answer += time + job[1]
            time = job[0] + job[1]
            continue
        if time > job[0]:
            answer += job[1]
            time = (job[0] + time)

    return answer


print(solution([[0, 3], [1, 9], [2, 6]]))