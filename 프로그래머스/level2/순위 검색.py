from collections import defaultdict
from itertools import combinations


def lower_bound(start, end, lst, target_score):
    while start < end:
        mid = (start + end) // 2
        if lst[mid] >= target_score:
            end = mid
        elif lst[mid] < target_score:
            start = mid + 1
    return start


def solution(info, queries):
    dic = defaultdict(list)
    for person in info:
        tmp = person.split(" ")
        condition = tmp[:-1]
        score = int(tmp[-1])
        for i in range(5):
            candidates = list(combinations([0, 1, 2, 3], i))
            for c in candidates:
                candidate = condition.copy()
                for j in c:
                    candidate[j] = '-'
                dic[' '.join(candidate)].append(score)

    for val in dic.values():
        val.sort()

    answer = []
    for query in queries:
        query = query.replace(' and ', ' ')
        query = query.split(' ')
        target_key = ' '.join(query[:-1])
        target_score = int(query[-1])
        count = 0
        if target_key in dic.keys():
            lst = dic[target_key]
            idx = lower_bound(0, len(lst), lst, target_score)
            count = len(lst) - idx
        answer.append(count)

    print(answer)
    return answer


solution(["java backend junior pizza 150","python frontend senior chicken 210","python frontend senior chicken 150","cpp backend senior pizza 260","java backend junior chicken 80","python backend senior chicken 50"],
         ["java and backend and junior and pizza 100","python and frontend and senior and chicken 200","cpp and - and senior and pizza 250","- and backend and senior and - 150","- and - and - and chicken 100","- and - and - and - 150"])