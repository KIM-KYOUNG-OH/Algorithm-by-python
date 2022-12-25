from itertools import permutations


def solution(k, dungeons):
    candidates = permutations(dungeons)
    answer = 0
    for candidate in candidates:
        tmp = k
        cnt = 0
        for need, minus in candidate:
            if tmp < need:
                break
            else:
                cnt += 1
                tmp -= minus
        answer = max(answer, cnt)
    return answer


print(solution(80, [[80,20],[50,40],[30,10]]))