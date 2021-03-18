from collections import deque

def solution(priorities, location):
    answer = 0
    q = deque([(idx,value) for idx,value in enumerate(priorities)])

    while q:
        temp = q.popleft()
        if max([i[1] for i in q]) > temp[1]:
            q.append(temp)
        else:
            answer += 1
            if temp[0] == location:
                break

    return answer

print(solution([1, 1, 9, 1, 1, 1], 0))