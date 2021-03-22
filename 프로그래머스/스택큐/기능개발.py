from collections import deque

def solution(progresses, speeds):
    answer = []
    progresses = deque(progresses)
    speeds = deque(speeds)
    day = 0
    count = 0
    while len(progresses) > 0:
        if (progresses[0] + speeds[0] * day) >= 100:
            progresses.popleft()
            speeds.popleft()
            count += 1
        else:
            if count > 0:
                answer.append(count)
                count = 0
            day += 1
    answer.append(count)

    return answer