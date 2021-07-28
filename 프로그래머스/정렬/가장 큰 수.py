# def solution(numbers):
#     numbers_str = list(map(str, numbers))
#     numbers_str.sort(key=lambda x: x*3, reverse=True)
#     return str(int(''.join(numbers_str)))

def solution(numbers):
    numbers_str = list(map(str, numbers))  # 문자열 타입으로 변환
    numbers_str.sort(key=lambda x: x * 3, reverse=True)  # 성분이 최대 1000이므로 최소 3자리수까지 맞춰서 비교
    return str(int(''.join(numbers_str)))  # 배열 성분들 문자열로 합치기


print(solution([3, 30, 34, 5, 9]))
