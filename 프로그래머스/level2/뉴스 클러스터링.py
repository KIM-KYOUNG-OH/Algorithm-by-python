from collections import Counter
import math


def solution(str1, str2):
    a = str1.lower()
    b = str2.lower()
    if a == b:
        return 65536

    a_list = []
    b_list = []
    for i in range(len(a) - 1):
        tmp = a[i: i + 2]
        if tmp.isalpha():
            a_list.append(tmp)
    for i in range(len(b) - 1):
        tmp = b[i: i + 2]
        if tmp.isalpha():
            b_list.append(tmp)

    a_counter = Counter(a_list)
    b_counter = Counter(b_list)

    inter = len(list((a_counter & b_counter).elements()))
    union = len(list((a_counter | b_counter).elements()))

    if union == 0:
        return 0
    jacad = math.floor((inter / union) * 65536)
    return jacad


print(solution('E=M*C^2', 'e=m*c^2'))


