def solution(numbers):
    answer = []
    
    for i in range(len(numbers)):
        for j in range(i+1, len(numbers)):
            a = (numbers[i]+numbers[j])
            if not(a in answer):
                answer.append(a)
    answer.sort()
    print(answer)
    return answer
    
numbers = [2,1,3,4,1]
solution(numbers)