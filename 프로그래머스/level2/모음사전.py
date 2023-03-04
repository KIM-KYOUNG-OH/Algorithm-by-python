from itertools import product


def solution(word):
    alps = ['A', 'E', 'I', 'O', 'U']
    answer = []
    for i in range(1, 6):
        candidates = product(alps, repeat=i)
        for candidate in candidates:
            answer.append(''.join(candidate))
    answer.sort()
    return answer.index(word) + 1
