def solution(brown, yellow):
    answer=[]
    x = (4+brown+((4+brown)**2-16*(brown+yellow))**0.5)/4
    y = (brown+yellow)/x
    temp = [int(x),int(y)]
    answer.append(max(temp))
    answer.append(min(temp))
    return answer

print(solution(10, 2))