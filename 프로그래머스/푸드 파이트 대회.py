def solution(food):
    for i in range(1, len(food)):
        if food[i] % 2 != 0:
            food[i] -= 1
    answer = ''
    for i in range(1, len(food)):
        answer += str(i) * (food[i] // 2)

    answer += '0'

    for i in range(len(food) - 1, 0, -1):
        answer += str(i) * (food[i] // 2)

    return answer


solution([1, 3, 4, 6])