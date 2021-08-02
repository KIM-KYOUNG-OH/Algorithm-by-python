# def solution(brown, yellow):
#     answer=[]
#     x = (4+brown+((4+brown)**2-16*(brown+yellow))**0.5)/4
#     y = (brown+yellow)/x
#     temp = [int(x),int(y)]
#     answer.append(max(temp))
#     answer.append(min(temp))
#     return answer

def solution(brown, yellow):
    answer = []
    # 연립 이차방정식의 근의 공식
    x = int((brown + 4 + ((brown + 4) ** 2 - 16 * (brown + yellow)) ** 0.5) / 4)
    y = int((brown + yellow) / x)
    answer = [max(x, y), min(x, y)]
    return answer


print(solution(10, 2))