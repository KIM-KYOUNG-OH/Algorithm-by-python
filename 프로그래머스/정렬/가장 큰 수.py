def solution(numbers):
    numbers_str = list(map(str, numbers))
    numbers_str.sort(key=lambda x: x*3, reverse=True)
    return str(int(''.join(numbers_str)))


print(solution([3, 30, 34, 5, 9]))
