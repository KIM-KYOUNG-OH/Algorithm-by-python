from collections import Counter


def solution(a):
    most_common = Counter(a).most_common()
    answer = 0
    for i in range(len(most_common)):
        if most_common[i][1] * 2 < answer:
            continue
        cur = most_common[i][0]
        subsequences = []
        tmp = []
        for j in a:
            if not tmp:
                tmp.append(j)
            else:
                if tmp[0] == cur:
                    if j != cur:
                        tmp.append(j)
                        subsequences.append(tmp)
                        tmp = []
                else:
                    if j == cur:
                        tmp.append(j)
                        subsequences.append(tmp)
                        tmp = []
        answer = max(answer, len(subsequences) * 2)
    return answer


# print(solution([0]))
# print(solution([5,2,3,3,5,3]))
# print(solution([0,3,3,0,7,2,0,2,2,0]))