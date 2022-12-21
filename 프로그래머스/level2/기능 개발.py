def solution(progresses, speeds):
    rest = []
    for i in range(len(progresses)):
        diff = 100 - progresses[i]
        if diff % speeds[i] == 0:
            rest.append(diff // speeds[i])
        else:
            rest.append((diff // speeds[i]) + 1)
    cur = rest[0]
    cnt = 1
    answer = []
    for i in range(1, len(rest)):
        if cur < rest[i]:
            cur = rest[i]
            answer.append(cnt)
            cnt = 1
        else:
            cnt += 1
    answer.append(cnt)
    return answer


print(solution([93, 30, 55], [1, 30, 5]))
print(solution([95, 90, 99, 99, 80, 99], [1, 1, 1, 1, 1, 1]))
