def solution(prices):
    answer = [0] * len(prices)

    for i in range(len(prices)-1):
        for j in range(i, len(prices)-1):
            print(i, j)
            if prices[i] > prices[j+1]:
                answer[i] += 1
                break
            else:
                answer[i] +=1
    return answer

print(solution([1, 2, 3, 2, 3]))