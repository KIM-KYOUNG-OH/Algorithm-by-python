# import heapq
#
# def solution(operations):
#     lst = []
#     answer = []
#     for i in range(len(operations)):
#         if operations[i] == "D -1":
#             if lst:
#                 heapq.heappop(lst)
#         elif operations[i] == "D 1":
#             if lst:
#                 lst.remove(max(lst))
#         else:
#             temp = list(operations[i].split(" "))
#             heapq.heappush(lst, int(temp[1]))
#     if len(lst) == 0:
#         return [0,0]
#     answer.append(max(lst))
#     answer.append(heapq.heappop(lst))
#     return answer

import heapq


def solution(operations):
    answer = []
    heap = []
    for oper in operations:
        if oper == 'D 1':  # 힙의 최대값 삭제
            if not heap:  # 큐가 비어있으면 continue
                continue
            heap.remove(max(heap))
        elif oper == 'D -1':  # 최소힙 root값 삭제
            if not heap:  # 큐가 비어있으면 continue
                continue
            heapq.heappop(heap)
        else:  # 숫자 삽입
            oper = oper.split()
            heapq.heappush(heap, int(oper[1]))
    if not heap:
        return [0,0]
    answer.append(max(heap))
    answer.append(heapq.heappop(heap))
    return answer


print(solution(["I 16", "I -5643", "D -1", "D 1", "D 1", "I 123", "D -1"]))