from itertools import combinations
from collections import Counter


def solution(orders, course):
    answer = []
    for i in course:
        candidates = []
        for order in orders:
            for case in combinations(order, i):
                candidates.append(''.join(sorted(case)))
        candidates_sorted = Counter(candidates).most_common()
        for s, cnt in candidates_sorted:
            if cnt > 1 and cnt == candidates_sorted[0][1]:
                answer.append(s)
            else:
                break
    return sorted(answer)


print(solution(["ABCFG", "AC", "CDE", "ACDE", "BCFG", "ACDEH"], [2,3,4]))