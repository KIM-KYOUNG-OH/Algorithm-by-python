def solution(n, left, right):
    answer = []
    for i in range(left, right + 1):
        share = i // n
        remainder = i % n
        bigger = share
        if share < remainder:
            bigger = remainder
        answer.append(bigger + 1)
    return answer

solution(4, 7, 14)