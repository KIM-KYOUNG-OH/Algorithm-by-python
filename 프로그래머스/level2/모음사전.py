from itertools import product


def solution(word):
    alps = ['A', 'E', 'I', 'O', 'U']
    lst = []
    for i in range(1, 6):
        for e in product(alps, repeat=i):
            lst.append(''.join(e))
    lst.sort()
    return lst.index(word) + 1

