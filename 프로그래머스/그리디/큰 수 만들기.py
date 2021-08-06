# def solution(number, k):
#     stack = []
#     for i in number:
#         while stack and i > stack[-1]:
#             if k > 0:
#                 stack.pop()
#                 k -= 1
#             else:
#                 break
#         stack.append(i)
#
#     if k > 0:
#         for _ in range(k):
#             stack.pop()
#
#     return "".join(stack)

def solution(number, k):
    stack = []
    for num in number:  # number의 앞에서부터 작은값 k개 뽑기
        while stack and num > stack[-1]:
            if k > 0:
                stack.pop()
                k -= 1
            else:
                break
        stack.append(num)

    while k > 0:  # number가 오름차순이라 삭제할 횟수가 남았을 때
        stack.pop()
        k -= 1

    return ''.join(stack)


print(solution("4177252841",4))