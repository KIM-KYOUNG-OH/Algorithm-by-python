from collections import deque

def solution(bridge_length, weight, truck_weights):
    bridge = [0] * bridge_length
    q = deque(bridge)
    tw = deque(truck_weights)
    second = 0
    while q:
        second += 1
        q.popleft()
        if tw:
            if sum(q) + tw[0] <= weight:
                q.append(tw.popleft())
            else:
                q.append(0)

    return second

print(solution(2,10,[7,4,5,6]))