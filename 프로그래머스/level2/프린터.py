from collections import deque


def solution(priorities, location):
    q = deque()
    for i in range(len(priorities)):
        q.append((i, priorities[i]))

    cnt = 1
    while q:
        idx, priority = q.popleft()
        if priority >= max(priorities):
            if idx == location:
                return cnt
            else:
                cnt += 1
            priorities.remove(priority)
        else:
            q.append((idx, priority))


print(solution([1, 1, 9, 1, 1, 1], 0))