# from collections import deque
#
#
# def solution(numbers, target):
#     answer = 0
#     q = deque()
#     q.append((0, numbers[0]))
#     q.append((0, -1 * numbers[0]))
#     while q:
#         idx, total = q.popleft()
#         idx += 1
#         if idx < len(numbers):
#             q.append((idx, total + numbers[idx]))
#             q.append((idx, total - numbers[idx]))
#         else:
#             if total == target:
#                 answer += 1
#
#     return answer





def solution(numbers, target):
    def dfs(depth, total):
        if depth == len(numbers):
            if total == target:
                answer[0] += 1
            return

        dfs(depth + 1, total + numbers[depth])
        dfs(depth + 1, total - numbers[depth])

    answer = [0]
    dfs(0, 0)
    return answer[0]


print(solution([1, 1, 1, 1, 1], 3))