from bisect import bisect_left
from itertools import combinations


def solution(info, query):
    answer = []
    info_dict = dict()

    for i in range(len(info)):
        candidate = info[i].split()
        key = candidate[:-1]
        value = int(candidate[-1])

        for j in range(5):
            for candidates in combinations(key, j):
                key_fixed = ''.join(sorted(candidates))
                if key_fixed not in info_dict:
                    info_dict[key_fixed] = [value]
                else:
                    info_dict[key_fixed].append(value)

    for k in info_dict:
        info_dict[k].sort()

    for qu in query:
        candidate = qu.split(' ')
        key = candidate[:-1]
        value = int(candidate[-1])

        while 'and' in key:
            key.remove('and')
        while '-' in key:
            key.remove('-')
        key_fixed = ''.join(sorted(key))

        if key_fixed in info_dict:
            scores = info_dict[key_fixed]
            except_idx = bisect_left(scores, value)
            answer.append(len(scores) - except_idx)
        else:
            answer.append(0)
    return answer


print(solution(["java backend junior pizza 150","python frontend senior chicken 210","python frontend senior chicken 150","cpp backend senior pizza 260","java backend junior chicken 80","python backend senior chicken 50"],
               ["java and backend and junior and pizza 100","python and frontend and senior and chicken 200","cpp and - and senior and pizza 250","- and backend and senior and - 150","- and - and - and chicken 100","- and - and - and - 150"]))