def solution(numbers):
    answer = []
    for num in numbers:
        lst = list('0' + bin(num)[2:])
        idx = ''.join(lst).rfind('0')
        lst[idx] = '1'

        if num % 2 == 1:
            lst[idx + 1] = '0'
        answer.append(int(''.join(lst), 2))
    return answer


solution([2,7])