from itertools import permutations


def solution(ads):
    answer = 0
    for candidate in permutations(ads, len(ads)):
        temp = 0
        current_time = candidate[0][0]
        for i in range(len(candidate)):
            temp += (current_time - candidate[i][0]) * candidate[i][1]
            current_time += 5
        answer = min(answer, temp)
    return answer
