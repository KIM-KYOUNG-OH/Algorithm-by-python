# import collections
#
# def solution(numbers, target):
#     answer = 0
#     # [현재까지 합, 합한 성분 개수]
#     q = collections.deque([(0, 0)])
#     # 큐가 다 비워질때까지
#     while q:
#         current_sum, num_idx = q.popleft()
#
#         if num_idx == len(numbers):
#             if current_sum == target:
#                 answer += 1
#         else:
#             # 하나 빼고 두개 생성
#             number = numbers[num_idx]
#             q.append((current_sum+number, num_idx + 1))
#             q.append((current_sum-number, num_idx + 1))
#
#     return answer

# def solution(numbers, target):
#     def dfs(idx, result):
#         if idx == len(numbers):
#             if result == target:
#                 nonlocal answer
#                 answer += 1
#             return
#         dfs(idx + 1, result + numbers[idx])
#         dfs(idx + 1, result - numbers[idx])
#         return
#
#     answer = 0
#     dfs(0, 0)
#     return answer

from collections import deque

def solution(numbers, target):
    answer = 0
    q = deque([(0, 0)])
    while q:
        result, idx = q.popleft()
        if idx == len(numbers):
            if result == target:
                answer += 1
            continue
        q.append((result + numbers[idx], idx + 1))
        q.append((result - numbers[idx], idx + 1))
    return answer


print(solution([1, 1, 1, 1, 1], 3))