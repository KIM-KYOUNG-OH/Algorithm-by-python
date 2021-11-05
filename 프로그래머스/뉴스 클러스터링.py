from math import floor


def divide(s):
    lst = []
    for i in range(0, len(s) - 1):
        temp = s[i:i + 2].upper()
        breaker = False
        for ch in temp:
            if ord(ch) not in [j for j in range(65, 91)]:
                breaker = True
                break
        if breaker:
            continue
        lst.append(temp)
    return lst


def union(a: list, b: list):
    a, b = a.copy(), b.copy()
    for i in a:
        if i in b:
            b.remove(i)
    return a + b


def intersection(a: list, b: list):
    a, b = a.copy(), b.copy()
    result = []
    for i in a:
        if i in b:
            result.append(i)
            b.remove(i)
    return result


def solution(str1, str2):
    lst1, lst2 = divide(str1), divide(str2)
    if len(lst1) == 0 and len(lst2) == 0:
        return 65536
    aa = len(intersection(lst1, lst2))
    bb = len(union(lst1, lst2))
    answer = floor(aa / bb * 65536)
    return answer


print(solution("aa1+aa2", "AAAA12"))