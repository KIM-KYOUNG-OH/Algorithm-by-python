# def solution(prices):
#     answer = [0] * len(prices)
#
#     for i in range(len(prices)-1):
#         for j in range(i, len(prices)-1):
#             print(i, j)
#             if prices[i] > prices[j+1]:
#                 answer[i] += 1
#                 break
#             else:
#                 answer[i] +=1
#     return answer

def solution(prices):
    answer = [0] * len(prices)  # 가격이 떨어지지 않은 연속 횟수 전부 0으로 초기화
    for i in range(len(prices) - 1):  # 마지막은 항상 0이므로 len(prices) - 1 번까지 순회
        for j in range(i, len(prices) - 1):
            answer[i] += 1
            if prices[i] > prices[j + 1]:  # 가격이 떨어졌을 경우 반복문 탈출
                break

    return answer


print(solution([1, 2, 3, 2, 3]))