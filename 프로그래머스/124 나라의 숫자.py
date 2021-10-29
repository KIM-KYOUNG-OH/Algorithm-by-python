def convert(elements, num):
    if num <= 3:
        return elements[num % 3 - 1]
    return convert(elements, (num - 1) // 3) + elements[num % 3 - 1]


def solution(n):
    numbers = ['1', '2', '4']
    answer = convert(numbers, n)
    return answer


print(solution(6))