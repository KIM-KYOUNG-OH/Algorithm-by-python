def solution(jobs):
    answer, now, i = 0, 0, 0  # 총 작업시간, 현재시간, jobs의 index
    heap = []

    return int(answer/len(jobs))


print(solution([[0, 3], [1, 9], [2, 6]]))