def solution(N, number):
    candidate_list = []

    for cnt in range(1, 9):
        candidate = set()
        candidate.add(int(str(N) * cnt))
        for i in range(cnt - 1):
            for left in candidate_list[i]:
                for right in candidate_list[-1 - i]:
                    candidate.add(left + right)
                    candidate.add(left - right)
                    candidate.add(left * right)
                    if right != 0:
                        candidate.add(left // right)
        if number in candidate:
            return cnt
        candidate_list.append(candidate)
    return -1