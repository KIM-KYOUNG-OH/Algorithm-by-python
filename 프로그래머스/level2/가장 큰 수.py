def solution(numbers):
    numbers = map(str, numbers)
    numbers = sorted(numbers, key=lambda x: x * 3, reverse=True)
    return ''.join(numbers)


print(solution([0, 0, 0]))